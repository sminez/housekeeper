'''
Our custom housekeeper Alexa skill
'''
import concurrent.futures

from flask import Flask
from flask_ask import Ask, statement

from todoist import TodoistAPI
from cal import events, describe
from secrets import todoist, calendars


# Top level Flask app
app = Flask(__name__)
ask = Ask(app, "/")


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
    all_events = []

    # Use threading to fetch all of the calendar details at the same time
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        futures = (ex.submit(events, url) for (name, url) in calendars.items())
        for f in concurrent.futures.as_completed(futures):
            try:
                evts = f.result()
                if evts:
                    all_events.extend(evts)
            except Exception as e:
                # If something went wrong then skip that calendar
                pass

    if all_events:
        summaries = ' '.join(describe(sorted(all_events)))
        return statement(f"<speak>Here's what I found: {summaries}</speak>")

    return statement(
        ('<speak>It looks like there are no events in your'
         ' calendars for the upcoming week</speak>')
    )
