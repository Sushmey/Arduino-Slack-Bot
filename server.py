from flask import Flask, render_template
from flask import request
import serial
import time
from slack_bolt.adapter.flask import SlackRequestHandler
from data import getData
from slackbot import slack_bot   # import the bot logic

# Wrap Bolt app with Flask handler
handler = SlackRequestHandler(slack_bot)

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
	if request.method=='POST':
		print("Button clicked!")
		data = getData()
		return render_template('home.html',data=data)
	return render_template('home.html',data="Click to get data")

@app.route("/slack/commands", methods=["POST"])
def slack_commands():
	print("Button clicked!")
	# data = getData()
	return handler.handle(request)

# Events API
@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if(__name__=='__main__'):  #This is so that we can run it directly in debug mode
	app.run(host='0.0.0.0', port=3000)



