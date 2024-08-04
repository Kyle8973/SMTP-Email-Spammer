# Description: A Python Script To Send Random Spam Emails To A Specific Email Address
# Author: Kyle8773
# Date: 4th August 2024
# GitHub: https://github.com/Kyle8773/SMTP-Email-Spammer

# Imports
import smtplib # Used To Send Email
from email.mime.text import MIMEText # Used To Create Email Body
from email.mime.multipart import MIMEMultipart # Used To Create Email Message
import ssl # Used To Create A Secure SSL Context
import time # Used To Add Delay Between Sending Emails
import random # Used To Generate Random Subject & Body Content

def send_spam():
    # Email Server Configuration
    smtp_server = "smtp.gmail.com"  # SMTP Server Address
    port = 587  # Port for Gmail TLS
    sender_email = "Your_Email@gmail.com"  # Your Email
    receiver_email = "Some_Nerd@email.com"  # The Email of the Person You Want To Spam
    password = "App Password"  # App Password --> https://myaccount.google.com/apppasswords

    # Email Content Array
    subjects = [
        "Get Spammed Nerd", 
        "Spam Alert!", 
        "Surprise! More Spam", 
        "Important Message",
        "You've Got Spam",
        "Check This Out",
        "Spammy Greetings!"
        # Add More Email Subjects Here If You Wish
    ]

    # Email Body Array
    bodies = [
        "Spam Spam Spam", 
        "This is your daily spam dose.", 
        "Enjoy some spam!", 
        "Here's some spam for you.",
        "Another day, another spam.",
        "Hope you love spam!",
        "Your favorite spam, delivered!"
        # Add More Email Body Content Here If You Wish
    ]

    # Create A Secure SSL Context
    context = ssl.create_default_context()

    # Sent Email Count
    sent_email_count = 0  # Track the Number of Emails Sent

    # Loop to Send Emails
    while True:
        # Select Random Email Content From The Lists
        subject_content = random.choice(subjects)
        random_number = random.randint(1, 9876543210)  # Generate A Random Number To Prevent Email Threading
        subject = f"{subject_content} {random_number}"  # Random Subject & Random Number
        body = random.choice(bodies) # Random Body Content

        # Create Message & Set Headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add Body To Email
        message.attach(MIMEText(body, "plain"))

        try:
            # Connect To The SMTP Server
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)  # Secure The Connection
            server.login(sender_email, password)  # Login To Email Server
            server.sendmail(sender_email, receiver_email, message.as_string())
            
            # Increment the Number of Emails Sent
            sent_email_count += 1
            print(f"Email Sent -> Total Emails Sent: {sent_email_count}")  # Print Success Message & Log the Number of Emails Sent

        except Exception as e:
            print(f"Error: {e}")  # Print Error Message

        finally:
            server.quit()

        # Wait For Defined Number Of Seconds Before Sending The Next Email
        time.sleep(0)  # Change 0 To The Number of Seconds You Want To Wait Before Sending The Next Email, Default is 0 Seconds (No Delay)

# Send The Spam Email
if __name__ == "__main__":
    send_spam()
