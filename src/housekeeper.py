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
    Give an overview of what we are doing today
    '''
    # Use threading to fetch all of the calendar details at the same time
    def named_events(name, url):
        return (name, events(url))

    resp = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        futures = (
            ex.submit(named_events, name, url)
            for (name, url) in calendars.items()
        )

        for f in concurrent.futures.as_completed(futures):
            try:
                name, evts = f.result()
                data = f'{name} has {" ".join(describe(evts))}'
                resp.append(data)
            except Exception as e:
                pass

    if resp:
        txt = " <break time='1s' /> ".join(resp)
        return statement(f'<speak>{txt}</speak>')
    else:
        return statement(
            ('It looks like there are no events in your'
             ' calendars for the upcoming week')
        )
