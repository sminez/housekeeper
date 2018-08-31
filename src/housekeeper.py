'''
Our custom housekeeper Alexa skill
'''
from flask import Flask, render_template
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
    resp = []
    # Get calendar info
    for name, url in calendars.items():
        evts = events(url)
        if evts:
            e_str = ' '.join(describe(evts))
            resp.append(f'{name} has: {e_str}')

    if resp:
        txt = " <break time='1s' /> ".join(resp)
        return statement(f'<speak>{txt}</speak>')
    else:
        return statement(
            ('It looks like there are no events in your'
             ' calendars for the upcoming week')
        )
