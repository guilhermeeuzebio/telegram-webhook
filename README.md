# How to use

To use it you'll need a domain name, for that you can use ngrok:

https://ngrok.com/

See their documentation to learn how to use it. 

You need to have it for the port 8443. If you disere another one, see in the telegram documentation the ports it accept and chage it in the run.py script.

When you have a domain name you'll need to call the setWebHook method in the Bot API via the following url:

https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}

my_bot_token is the token that you recive when a bot is created in telegram, if you don't know how to create a bot in telegram see how in the following link:

https://core.telegram.org/bots#6-botfather

url_to_send_updates_to is your domain name

Example:

https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setWebhook?url=https://www.example.com/my-telegram-bot

Important to note that is necessary a https 

It's necessary to set two env variables:

TELEGRAM_TOKEN that is the bot token

BOT_URL that is the url to recive the messages and process it

Link to the telegram official API:

https://core.telegram.org/bots/api

Then to use it, run:

python3 run.py

Note that this commands are for Debian based Linux distributions, but you can use this source code with any other distribution or in windows

