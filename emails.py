#!/usr/bin/env python3

'''for generating the emails with attachments

Once the PDF is generated, you need to send the email using the emails.generate_email() and emails.send_email() methods.
Define generate_email and send_email methods by importing necessary libraries.

'''

import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path):
  message = email.message.EmailMessage()
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = recipient
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message


def send_email(the_message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(the_message)
  mail_server.quit()
