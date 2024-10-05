# Send messages to Signal with Python

This project was created to send Signal messages to a Signal account.
 
# Installation

## Install signal-cli
To use it you need to install the signal-cli from the following GitHub project.
https://github.com/AsamK/signal-cli

I suggest that you download one of the pre-compiled binaries from the following link:
https://github.com/AsamK/signal-cli/releases/tag/v0.13.7

Install it on your system. (You might need to install a later version of Java to get it going.)
You also need a Signal account. Signal can only be used on one device at a time. I used an old sim card for the signal server. Ensure that your sim card is active on your cell. In the registration process Signal will send an SMS to the sim card. You will have to enter the code from signal to activate Signal on your server.
## Verify and register your number on the system
After installation run the following commands from your terminal.
./signal-cli -u [yourcellnumber] register
(The format for [yourcellnumber] will be +[country code][the last 9 digits of your cell number])

You will get a response from the terminal similar to the following:

*Captcha required for verification, use --captcha CAPTCHA
To get the token, go to https://signalcaptchas.org/registration/generate.html
After solving the captcha, right-click on the "Open Signal" link and copy the link.*

Open the url in your browser and pass the Captcha check.
There will be a link on the page "Open Signal".
Right-click on the link and copy it. You will need it for the next step.
[copied captcha]
Run the following in your terminal:

./signal-cli -u [yourcellnumber] register --captcha [copied captcha]

Wait for the Signal SMS verification code that will be sent to your cell.
[smscode]

Run:

./signal-cli -u  [yourcellnumber] verify [smscode]

## install your Python Virtual environment
Run:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## create a .env file
Create a .env file in the root of the project (linux)
update the .env variables from the .env-example file.

# Usage 

run the main.py file from the terminal. 

python main.py

# Contact me

For any suggestions contact me:

Gert van Eeden

info@itinnovate.co.za

https://www.linkedin.com/in/gertvaneeden/









