'''
Our custom housekeeper Alexa skill
'''
from flask import Flask, render_template
from flask_ask import Ask, statement


# Top level Flask app
app = Flask(__name__)
ask = Ask(app, "/")


@ask.intent('daily-summary')
def daily_summary():
    '''
    Give an overview of what we are doing today
    '''
    pass
