# SMS Sender using Africa's Talking API(Python)

This script demonstrates how to send SMS messages using the Africa's Talking SMS Gateway API in Python.

## Usage

1. Clone Repo

  `git clone https://github.com/rungene/bulk-sms-africas-talking`

2. Create a virtual environment (venv)

  `python venv venv`

  - activate the virtual environment

  `source .venv/bin/activate`

3. Ensure you have set the following environment variables with appropriate values:
   - `api_key`: Your Africa's Talking API key.
   - `username`: Your Africa's Talking account username.

4. Install the required dependencies:

pip install -r requirements.txt

5. CSV File (Optional):
  - The script assumes the presence of a CSV file named sample.csv containing phone numbers.
  - You can modify the script to accept the CSV filename as an argument or read phone numbers from another source.

6. Call the `send_sms` function with the list of phone numbers and message content as arguments.

Example usage:
```python
import os
from server import send_sms
from read_phone_numbers import read_kenyan_phone_numbers
# Set up API credentials
os.environ['api_key'] = 'YOUR_API_KEY'
os.environ['username'] = 'YOUR_USERNAME'
```

# Define phone numbers and message content
phone_numbers = read_kenyan_phone_numbers()
message = "Welcome to Topp"

# Send SMS
send_sms(phone_numbers, message)

# Functionality
  - Retrieves only Kenyan Phone phone numbers (from CSV).
  - Assuming phone numbers are in the fourth column (index 3)
  - if the number starts with '0' its modified to start with '+254'
  - Constructs the SMS message with content and sender short code.
  - Sends the SMS message(s) to the provided phone numbers using the Africa's Talking API.
  - Parses the API response and indicates success or failure for each recipient.

# Additional Resources

- Africa's Talking Documentation: https://africastalking.com/sms

**License**

[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
