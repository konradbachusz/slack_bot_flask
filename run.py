# -*- coding: utf-8 -*-


from slackbot.bot import Bot,respond_to,listen_to
import os
import re
import json

from flask import Flask
from app import * 


# flask 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

# slack api token 
SLACKBOT_API_TOKEN = os.environ.get("SLACKBOT_API_TOKEN")


# running bot by flask 
#=======================================


def main():
    bot = Bot()
    bot.run()


@app.route('/')
def run_bot():
	bot = Bot()
 	bot.run()
	return 'RUN slack bot now' 


# Respond 
#=======================================

@respond_to('github', re.IGNORECASE)
def github():
    attachments = [
    {
        'fallback': 'Fallback text',
        'author_name': 'Author',
        'author_link': 'http://www.github.com',
        'text': 'Some text',
        'color': '#59afe1'
    }]
    message.send_webapi('', json.dumps(attachments))


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('data plz')
def data(message):
    df = sample_data()
    message.reply( "```"+str(df) + "```")

@respond_to('echo (.*)')
def echo_word(message,something):
    feedback = regular_response(something)
    message.reply(feedback)


@respond_to('Give me (.*)')
def giveme(message, something):
    message.reply('Here is {}'.format(something))


@respond_to('test now')
def test(message):
    message.reply('OK ROGER THAT !')


@listen_to('help me')
def help(message):
    message.reply('Yes, I can!')

#=======================================


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000,threaded=True,debug = True)
	#main()





