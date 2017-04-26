# -*- coding: utf-8 -*-


from slackbot.bot import Bot,respond_to,listen_to
import os
import re
import json

from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


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

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')


@respond_to('test now')
def test(message):
    message.reply('OK ROGER THAT !')

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    # message.send('I can help everybody!')

#=======================================


if __name__ == "__main__":
	app.run(host='0.0.0.0',threaded=True,debug = True)
	#main()





