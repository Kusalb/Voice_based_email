
import email
import imaplib
import speech_recognition as sr
import smtplib, ssl

username = 'gudkush007@gmail.com'
password = '#Bullet123!'
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)
mail.select('"[Gmail]/Sent Mail"')
counter = 0
# result, data = mail.uid('search', None, "ALL")
result, data = mail.search(None, 'ALL')

outbox_item_list = data[0].split()
list_message = []
for item in outbox_item_list:
    result2, email_data = mail.uid('fetch', item, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    # print(raw_email)
    email_message = email.message_from_string(raw_email)
    to_ = email_message['to']
    from_ = email_message['From']
    subject_ = email_message['Subject']
    date_ = email_message['date']
    counter = counter + 1
    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        content_type = part.get_content_type()
        if "plain" in content_type:
            msg = part.get_payload()
            # print(msg)
            outbox = {}
            outbox['to'] = to_
            outbox['from'] = from_
            outbox['subject'] = subject_
            outbox['date'] = date_
            outbox['message'] = msg
            outbox['id'] = counter
            print(outbox)