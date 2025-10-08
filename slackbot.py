from slack_bolt import App
from data import getData
from dotenv import load_dotenv
import threading
import os

load_dotenv()
# Initialize your app with bot token and signing secret
slack_bot = App(
    token=os.getenv('SLACK_TOKEN'),
    signing_secret=os.getenv('SLACK_SIGNING_SECRET')
)

# Example: Respond when someone says "hello"
@slack_bot.message("hello")
def say_hello(message, say):
    user = message['user']
    say(f"Hey there, <@{user}>! 👋")

@slack_bot.command("/gettemp")
def get_data(ack, respond):
    # Acknowledge immediately (Slack requires this within 3 seconds)
    ack()
    # user = message['user']
    def fetch_and_respond():
        data = getData()
        if(data!=None):
            respond(f"👋 Hello there, here is the data {data}!")
        else:
            respond(f"Sorry there's been an error! :( ")
    threading.Thread(target=fetch_and_respond).start()


# # Start the app
# if __name__ == "__main__":
#     slack_bot.start(port=3000)
