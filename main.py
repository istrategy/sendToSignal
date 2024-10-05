from sendsignal import send_signal_message


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    message = input("Enter your message: ")
    recipient_number = input("Enter the recipient cell number e.g. +27000000000: ")
    send_signal_message(message, recipient_number)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Execute')


