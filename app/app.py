from flask import Flask, request
import os
import requests
import json

app = Flask(__name__)

telegram_bot_token = os.environ['TELEGRAM_TOKEN']
url = "https://api.telegram.org/bot{}/".format(telegram_bot_token)
bot_url = os.environ['BOT_URL']
headers = {'Content-Type': 'application/json'}

def get_chat_id(update):
	chat_id = update['message']['chat']['id']
	return chat_id

def last_update(data):
	print(data)
	results = data['result']
	total_updates = len(results) - 1
	if results:
		return results[total_updates]
	else:
		return {}

def send_message(chat, text):
    params = {'chat_id': chat, 'text': "{}".format(text) }
    response = requests.post(self.url + 'sendMessage', data=params)
    print(response)
    return response

def send_to_bot(text):
	user_text = requests.post(bot_url, data=json.dumps(text), headers=headers)
	return user_text.json()

@app.route("/", methods=['POST'])
def post():
	try:
		client_request = request.get_json(silent=True)
	except Exception as e:
		pass

	if not client_request:
		return {'error': {'server didn\'t get any data to process'}, 'status': 400}

	if 'message' not in client_request:
		return {'error': {'server didn\'t get any data to process'}, 'status': 400}

	if 'text' not in client_request['message']:
		return {'error': {'server didn\'t get any data to process'}, 'status': 400}

	text = client_request["message"]["text"]
	response = send_to_bot(text)
	#print(response)
	#send_message(get_chat_id((response)
	return text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8443)
