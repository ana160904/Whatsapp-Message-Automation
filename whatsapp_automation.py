# whatsapp_scheduler.py

from twilio.rest import Client
from datetime import datetime
import time
import os



# STEP 1: TWILIO CREDENTIALS

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
#These two values are your Twilio API credentials.
#Python, get this value from my computer's environment variables." using os.get.....

#That's safer because you don't want to accidentally upload your API credentials to GitHub.

client = Client(ACCOUNT_SID, AUTH_TOKEN)
#Here we're creating an object using which clinet can communicate with twilio


# STEP 2: SEND WHATSAPP MESSAGE

def send_whatsapp_message(recipient_number, message_body):

    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            to=f"whatsapp:{recipient_number}",
            body=message_body
        )

        print(f"\nMessage sent successfully!")
        print(f"Message SID: {message.sid}")

    except Exception as e:
        print(f"\nError: {e}")



# STEP 3: GET USER INPUT


print("===== WhatsApp Message Scheduler =====\n")

recipient_name = input("Enter recipient name: ")

recipient_number = input(
    "Enter recipient WhatsApp number with country code "
    "(example: +919876543210): "
)

message_body = input(
    f"Enter the message you want to send to {recipient_name}: "
)



# STEP 4: GET DATE AND TIME


date_input = input(
    "\nEnter the date to send the message "
    "(YYYY-MM-DD): "
)

time_input = input(
    "Enter the time to send the message "
    "(24-hour format HH:MM): "
)



# STEP 5: CONVERT USER INPUT INTO DATETIME

try:

    scheduled_datetime = datetime.strptime(
        f"{date_input} {time_input}",
        "%Y-%m-%d %H:%M"
    )

except ValueError:

    print("\nInvalid date or time format.")
    print("Use:")
    print("Date -> YYYY-MM-DD")
    print("Time -> HH:MM")
    exit()



# STEP 6: CALCULATE DELAY


current_datetime = datetime.now()

delay = scheduled_datetime - current_datetime

delay_seconds = delay.total_seconds()

# STEP 7: CHECK IF TIME IS IN THE PAST


if delay_seconds <= 0:

    print("\nThe specified time is in the past.")
    print("Please enter a future date and time.")

    exit()


# STEP 8: WAIT UNTIL SCHEDULED TIME


print(
    f"\nMessage scheduled for "
    f"{scheduled_datetime.strftime('%Y-%m-%d %H:%M')}"
)

print(f"Waiting {int(delay_seconds)} seconds...")


time.sleep(delay_seconds)



# STEP 9: SEND THE MESSAGE


send_whatsapp_message(
    recipient_number,
    message_body
)
