'''
Our custom housekeeper Alexa skill
'''
from datetime import date
from calendar import monthcalendar, weekday

from flask import Flask
from flask_ask import Ask, statement

from utils import run_many
from cal import events, describe
from secrets import calendars

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
                    cal = monthcalendar(year, today.month-1)
                    month -= 1
                else:
                    cal = monthcalendar(year-1, 12)
                    month = 12
                    year -= 1

                monday = cal[-1][0]
                ix = cal[-1].index(today.day)
            break

    monday = date(year, month, monday)

    try:
        week_menu = MENUS[WEEKS[monday]]
    except KeyError:
        if weekday(today.day, today.month, today.year) > 4:
            # It's the weekend
            return statement(
                ("<speak>You silly sausage, it's the weekend!"
                 " You don't have school lunch at the weekend!</speak>")
            )
        else:
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
