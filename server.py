import os
from flask import Flask, request
import requests
from dotenv import load_dotenv
from read_phone_numbers import read_kenyan_phone_numbers

load_dotenv()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/sms_callback', methods=['POST'])
def sms_callback():
    print(request.method)
    print(request.form)
    # response_to_sms(request.form['from'], \
    # f"You texted me: {request.form['text']}")
    return 'Success', 201


api_key = os.getenv('api_key')
# Define API endpoint URL
url = 'https://api.sandbox.africastalking.com/version1/messaging'
username = os.getenv('username')
file_name = 'sample.csv'
phone_numbers = read_kenyan_phone_numbers(file_name)
message = "Welcome to Toppline Kenya"
myShortCode = 'Toppline Kenya'

# @app.route('/sms/send',  methods=['POST', 'GET'])
def send_sms(phone_numbers, message):
    """
    Sends an SMS message to a list of phone numbers using the Africa's Talking API.
    
    Args:
        phone_numbers (list): A list of phone numbers (strings) to send the SMS to.
        message (str): The message content to be sent.

    Return:
        None: This function does not return any value.
    Raises:
        Exception: If the SMS sending fails due to an error response from the API.
    """
    response = requests.post(
        url,
        data={
            'username': username,
            'to': ','.join(phone_numbers),
            'message': message,
            'from': myShortCode
        },
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'apiKey': api_key
        }
    )
    if response.status_code == 201:
        data = response.json()
        print(f'Received data {data}')
        response_list = data['SMSMessageData']['Recipients']
        for r in response_list:
            if r.get('statusCode') == 101:
                print('message sent success fully')
    else:
        print(f'Error: {response.status_code}')


if __name__ == '__main__':
    send_sms(phone_numbers, message)
