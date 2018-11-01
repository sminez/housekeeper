'''
Our custom housekeeper Alexa skill

See here for details on slot types
  >>> https://developer.amazon.com/docs/custom-skills/slot-type-reference.html
'''
from datetime import date, timedelta
from calendar import monthcalendar, weekday

from flask import Flask
from flask_ask import Ask, statement

from secrets import calendars
from utils import run_many, parse_amazon_date_to_range
from cal import events, describe, describe_relative, \
    all_calendar_events_in_range

from data.menus import autumn_2018_weeks as WEEKS
from data.menus import autumn_2018_menus as MENUS


# Top level Flask app
app = Flask(__name__)
ask = Ask(app, "/")


DAYS = [
    'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday',
    'Saturday', 'Sunday'
]


def lambda_handler(event, _context):
    '''
    Entrypoint for an incoming AWS Lambda event
    '''
    return ask.run_aws_lambda(event)


@ask.intent('daily_summary')
def daily_summary():
    '''
    Give an overview of what we are doing over the next 7 days.
    '''
    # Use threading to fetch all of the calendar details at the same time
    args = [(url,) for url in calendars.values()]
    all_events = sorted(sum(run_many(events, args), []))

    if all_events:
        summaries = ' '.join(describe(all_events))
        return statement(f"<speak>Here's what I found: {summaries}</speak>")

    return statement(
        ('<speak>It looks like there are no events in your'
         ' calendars for the upcoming week</speak>')
    )


@ask.intent('free_on_date', convert={'day': 'date'})
def free_on_date(day):
    '''
    Check to see if we are free on a given date.  The user can be quite
    abstract in their request, i.e. 'are we free the week of the 15th of
    october?' and Alexa _should_ be able to parse it.
    '''
    all_events = all_calendar_events_in_range(
        calendars.values(),
        day,
        day + timedelta(hours=24),
    )

    if len(all_events) > 0:
        summaries = ' '.join(describe_relative(all_events, day))
        return statement(
            (f'It looks like you are not free on {day}.'
             f' You have, {summaries}')
        )

    return statement(
        "I can't see anything in your calendars. Looks like you're free!"
    )


@ask.intent('availability', default={'name': None, 'time_range': None})
def availability(name, time_range):
    '''
    Either read or email our availability for a given time range.

    Not using flask_ask conversion here as we need to know if we are
    being asked about a day, week or month.
    '''
    start, stop = parse_amazon_date_to_range(time_range)
    all_events = all_calendar_events_in_range(calendars.values(), start, stop)
    event_days = {e.start.date() for e in all_events}
    all_days = {start + timedelta(days=d) for d in range((stop - start).days)}
    free_days = all_days - event_days

    if name is not None:
        # We are sending an email
        return statement("I haven't implemented sending an email yet")

    return statement(
        (f'You are free on {len(free_days)} days in {time_range}:'
         f' {", ".join(str(d) for d in free_days)}.')
    )


@ask.intent('lunch_today')
def lunch_today():
    '''
    Determine which menu Lila has to chose from on the given day and
    read her the options, including the standard items as well.
    '''
    today = date.today()
    month = today.month
    year = today.year
    cal = monthcalendar(year, month)

    # Check to see if it's the weekend...
    if weekday(today.year, today.month, today.day) > 4:
        return statement(
            ("<speak>You silly sausage, it's the weekend!"
             " You don't have school lunch at the weekend!</speak>")
        )

    # Find the date of Monday this week so we can determine which of the
    # three weekly menus we need to look at.
    for week in cal:
        if today.day in week:
            monday = week[0]
            ix = week.index(today.day)

            # This week started in the previous month so we need to
            # look at that calendar instead.
            if monday == 0:
                if today.month > 1:
                    _cal = monthcalendar(year, today.month-1)
                    month -= 1
                else:
                    _cal = monthcalendar(year-1, 12)
                    month = 12
                    year -= 1

                monday = _cal[-1][0]
            break

    monday = date(year, month, monday)

    try:
        week_menu = MENUS[WEEKS[monday]]
    except KeyError:
        if today < max(WEEKS.keys()):
            return statement(
                "<speak>Are you on half term silly sausage?</speak>"
            )

        return statement(
            ("<speak>I'm sorry, Daddy needs to give me the"
             " new menu! If you ask him nicely, he can get it for me"
             " and I can tell you what is for lunch tomorrow.</speak>")
        )

    # Get the data we need for the response
    today = DAYS[ix]
    main = week_menu['main'][ix]
    vegitarian = week_menu['vegitarian'][ix]
    sides = week_menu['sides'][ix]
    pudding = week_menu['pudding'][ix]

    return statement(
        (f'<speak>Here is the menu for {today} this week.'
         f' You can have baked potatoe, {main}, or {vegitarian}.'
         f' You will get some {sides} on the side as well.'
         f' For pudding you can have {pudding}, yoghurt,'
         f' or fresh fruit.</speak>')
    )
