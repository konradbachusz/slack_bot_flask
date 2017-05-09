# -*- coding: utf-8 -*-


from slackbot.bot import Bot,respond_to,listen_to
import os
import re
import json

from flask import Flask
from app import * 
from backup_msg_db import * 



# flask 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

# slack api token 
SLACKBOT_API_TOKEN = os.environ.get("SLACKBOT_API_TOKEN")



# sqlite objects 
# import from backup_msg_db
#=======================================



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



@respond_to('spotify (.*)')
def reply_album(message, artist):
    df = spotify_album(artist)
    message.reply("```" + 'ALBUM : {}'.format(df) +  "```")


@respond_to('test now (.*)')
def test(message,input):
    listing  =  input_msg(created = datetime.now(),
                          msg = str(input)) 
    session.add(listing)
    session.commit()
    message.reply('OK ROGER THAT !')



@respond_to('help me')
def help(message):
    message.reply('Yes, I can!')

@respond_to('sql backup')
def input_log(message):
    #listing = session.query(input_msg)
    history = ''
    for item in session.execute("select * from msg"):
        history += str(item) + "\n" 
    #print (session.fetchall())
    session.commit()
    #print (session)
    #print (listing)
    message.reply("OK")
    message.reply("```" + str(history) + "```")


#=======================================


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000,threaded=True,debug = True)
	#main()





