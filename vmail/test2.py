import email
import imaplib
import mimetypes

from bs4 import BeautifulSoup
import os

username = 'kbista.logispark@gmail.com'
password = '#Bullet123!'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)
mail.select("inbox")
counter =0
result, data = mail.uid('search', None, "ALL")
inbox_item_list = data[0].split()

for item in inbox_item_list:
    result2, email_data = mail.uid('fetch', item, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    to_ = email_message['To']
    from_ = email_message['From']
    subject_ = email_message['Subject']
    date_ = email_message['date']
    counter = counter + 1
    counter_ = email_message['counter']
    print(counter)

    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        content_type = part.get_content_type()
        if "plain" in content_type:
            p = part.get_payload()

            # print(p)
            # print(to_)
            # print(from_)
            # print(subject_)
            # print(date_)
            pass


# # Import the required module for text
# # to speech conversion
# from gtts import gTTS
#
# # This module is imported so that we can
# # play the converted audio
# import os
#
# # The text that you want to convert to audio
# mytext = 'Verify'
#
# # Language in which you want to convert
# language = 'en'
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("verify.mp3")
import smtplib, ssl, imaplib
#
# import smtplib, ssl
#
# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "kbista.logispark@gmail.com "
# receiver_email = "kunalbista25@gmail.com"
# password = '#Bullet123!'
#
# dict = {}
#
# message = 'Hello this is test mail.'
# subject = 'Hi there bhayo'
#
# dict['message'] = message
# dict['receiver_mail'] = receiver_email
# dict['subject'] = subject
#
# message = "\r\n".join(["Subject:" + dict['subject'], "", dict['message']])
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
