import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_signal_message(message, recipient_number):
    # Load the variables from the environment
    signal_cli_path = os.getenv('SIGNAL_CLI_PATH')  # Signal CLI path from .env
    sender_number = os.getenv('SENDER_NUMBER')  # Sender's phone number from .env


    try:
        # Command to send a message via Signal CLI
        command = [
            signal_cli_path,  # Path to signal-cli executable
            '-u', sender_number,  # Sender's phone number (registered Signal number)
            'send',
            '-m', message,  # The message you want to send
            recipient_number  # Recipient's phone number
        ]

        # Run the command and capture output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check if the message was sent successfully
        if result.returncode == 0:
            print("Message sent successfully!")
            print(result.stdout.decode())  # Prints the success message from signal-cli
        else:
            print("Failed to send message.")
            print(result.stderr.decode())  # Prints error details

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
#send_signal_message("Hello from Python!", os.getenv('RECIPIENT_NUMBER'))
