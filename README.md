# Arduino-Slack-Bot
A Slack bot that fetches and displays the current climate conditions of my room using data from an Arduino device.

---

## Overview

This project combines a Flask API and a Slack bot to deliver real-time climate data directly to your Slack workspace.

The Flask server communicates with your Arduino to fetch the data, while the Slack bot listens for user commands and responds with the fetched values.

The Flask API is made publicly accessible to Slack using **ngrok**, which provides a secure tunnel to your local environment.

---
## Architecture

Here’s how the system flows:
```
User (Slack) → ngrok (public URL) → Flask (localhost:5000)
```

- **Flask Server (port 5000):** Hosts the API endpoint that retrieves the Arduino sensor data.  
- **ngrok:** Exposes the Flask API to the internet with a temporary HTTPS URL.  
- **Slack Bot:** Uses the ngrok URL to send slash command requests to the Flask server.  

Internally, the Flask script initializes the Slack bot, which defines the endpoints that Slack will hit.

The logic for handling Slack commands is in `slackbot.py`.  
When a user invokes the Slack command (e.g. `/gettemp`), the bot:
1. Connects to the Arduino,  
2. Fetches the temperature and humidity data, and  
3. Returns the results as a Slack message.



## Steps to run

Start the flask server
```
python server.py --host=0.0.0.0 --port=5000
```

Start the ngrok server at port 3000 (or any other that 5000)
```
ngrok 3000
```

Add the endpoint from ngrok for Slack to connect to in events and commands.
