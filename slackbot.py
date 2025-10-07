from slack_bolt import App
from data import getData
import threading

# Initialize your app with bot token and signing secret
slack_bot = App(
    token="",
    signing_secret=""
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
        respond(f"👋 Hello there, here is the data {data}!")
    threading.Thread(target=fetch_and_respond).start()


# # Start the app
# if __name__ == "__main__":
#     slack_bot.start(port=3000)
