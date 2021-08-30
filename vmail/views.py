from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
import pyttsx3
import email
import imaplib
import speech_recognition as sr
import smtplib, ssl
from gtts import gTTS
import os
from django.contrib.auth import authenticate, login, logout

# !/usr/bin/env python
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

import os
import pyaudio
import wave
import audioop
from collections import deque
import time
import math

# from vmail.models import Poll
from vmail.models import Compose, Inbox, Draft, Notification

data_dict = {'username': '', 'password': '', 'recipent': '', 'message': '', 'subject': '', }

def index(request):
    # engine = pyttsx3.init()  # object creation
    # """ RATE"""
    # rate = engine.getProperty('rate')  # getting details of current speaking rate
    # print(rate)  # printing current voice rate
    # engine.setProperty('rate', 125)  # setting up new voice rate
    # """VOLUME"""
    # volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    # print(volume)  # printing current volume level
    # engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    # """VOICE"""
    # voices = engine.getProperty('voices')  # getting details of current voice
    # # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    # engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    # engine.say("Welcome, to voice based email system")
    # engine.say("Single left click to compose a mail.")
    # # engine.say('My current speaking rate is ' + str(rate))
    # engine.runAndWait()
    # engine.stop()
    return render(request, 'vmail/home.html')


def voicetotext(request):
    text = []
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    value = text
    return render(request, 'vmail/compose.html', {'value': value})


def compose_message(request):
    text = []
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly

    value = text
    print(text)
    try:
        data_dict['message'] = value
        engine = pyttsx3.init()  # object creation
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        engine.setProperty('rate', 125)  # setting up new voice rate
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        engine.say(value)
        engine.runAndWait()
        engine.stop()
    except:
        print('error')
    return render(request, 'vmail/compose.html', {'value': value})


def compose_subject(request):
    text = []
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    value = text
    print(text)
    try:
        data_dict['subject'] = value
        engine = pyttsx3.init()  # object creation
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        engine.setProperty('rate', 125)  # setting up new voice rate
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        engine.say(value)
        engine.runAndWait()
        engine.stop()
    except:
        return render(request, 'vmail/compose.html')
    return render(request, 'vmail/compose.html', {'value': value})


def compose_recipent(request):
    text = []
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly

    print(text)
    try:
        value = text.replace(' ', '')
        data_dict['recipent'] = value
        engine = pyttsx3.init()  # object creation
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        engine.setProperty('rate', 200)  # setting up new voice rate
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        for i in value:
            engine.say(i)
        engine.runAndWait()
        engine.stop()
    except:
        print('sorry')
        return render(request, 'vmail/compose.html')

    return render(request, 'vmail/compose.html', {'value': value})


def compose_send1(request):
    inbox_dict = {
        'inbox': data_dict
    }
    return render(request, 'vmail/send.html', inbox_dict)


def compose_send(request):
    print('here')
    sub = data_dict['subject']
    to = data_dict['recipent']
    msg = data_dict['message']

    print(sub)
    print(to)
    print(msg)
    message = Compose.objects.create(to=data_dict['recipent'], subject=data_dict['subject'],
                                     message=data_dict['message'])
    message.save
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = data_dict['username']
    password = data_dict['password']
    receiver_email = to
    message = "\r\n".join(["Subject:" + sub, "", msg])
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    inbox_dict = {
        'inbox': data_dict
    }
    return render(request, 'vmail/compose.html', inbox_dict)


def compose_discard(request):
    sub = ''
    to = ''
    msg =''
    sub = data_dict['subject']
    to = data_dict['recipent']
    msg = data_dict['message']
    print(sub)
    print(to)
    print(msg)
    msgobject = Draft.objects.create(to=data_dict['recipent'], subject=data_dict['subject'],
                                     message=data_dict['message'])
    msgobject.save
    return render(request, 'vmail/home.html')


def compose(request):
    return render(request, 'vmail/compose.html')

def inbox(request):
    username = 'kushaltech45@gmail.com'
    password = 'password 1234 @'

    # username = data_dict['username']
    # password = data_dict['password']
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    counter = 0
    result, data = mail.uid('search', None, "ALL")
    inbox_item_list = data[0].split()
    list_message = []
    for item in inbox_item_list:
        result2, email_data = mail.uid('fetch', item, '(RFC822)')
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        to_ = email_message['To']
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
                inbox = {}
                inbox['to'] = to_
                inbox['from'] = from_
                inbox['subject'] = subject_
                inbox['date'] = date_
                inbox['message'] = msg
                inbox['id'] = counter
                list_message.append(inbox)

    inbox_message = list_message
    print(inbox_message.reverse())
    cou = len(list_message)
    print(cou)
    co = Notification.objects.create( note= cou)
    co.save
    getc = Notification.objects.all().count()
    print(getc)
    getcount = Notification.objects.last()
    idc = getcount.id - 1
    print(idc)
    getdatac = Notification.objects.filter(id = idc)
    val = 0
    for i in getdatac:
        val = i.note
    print(val)
    notifica = ( getcount.note - val )
    return render(request, 'vmail/inbox.html', {'inbox': inbox_message, 'noti': notifica})




def outbox(request):
    username = 'kushaltech45@gmail.com'
    password = 'password 1234 @'
    # username = data_dict['username']
    # password = data_dict['password']
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
        print(raw_email)
        email_message = email.message_from_string(raw_email)
        to_ = email_message['to']
        bcc = email_message['Bcc']
        print(bcc)
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
                outbox = {}
                outbox['to'] = to_
                outbox['from'] = from_
                outbox['subject'] = subject_
                outbox['date'] = date_
                outbox['message'] = msg
                outbox['bcc'] = bcc
                print(msg)
                outbox['id'] = counter
                list_message.append(outbox)
    print(list_message)
    outbox_messages = list_message.reverse()
    print('here')
    print(outbox_messages)
    return render(request, 'vmail/outbox.html', {'outbox': list_message})


def draft(request):
    draft = Draft.objects.all().order_by('-id')
    return render(request, 'vmail/draft.html', {'draft': draft})


def password(request):
    text = []
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
            value = text
            print(text)
            data_dict['password'] = value
            engine = pyttsx3.init()  # object creation
            rate = engine.getProperty('rate')  # getting details of current speaking rate
            print(rate)  # printing current voice rate
            engine.setProperty('rate', 200)  # setting up new voice rate
            volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
            print(volume)  # printing current volume level
            engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
            voices = engine.getProperty('voices')  # getting details of current voice
            engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
            for i in value:
                engine.say(i)
            engine.runAndWait()
            engine.stop()
            return render(request, 'vmail/login.html', {'value': value})
        except:
            engine = pyttsx3.init()  # object creation
            rate = engine.getProperty('rate')  # getting details of current speaking rate
            print(rate)  # printing current voice rate
            engine.setProperty('rate', 125)  # setting up new voice rate
            volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
            print(volume)  # printing current volume level
            engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
            voices = engine.getProperty('voices')  # getting details of current voice
            engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
            engine.say('Could not recognize')
            engine.runAndWait()
            engine.stop()
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
            return render(request, 'vmail/login.html')
        return render(request, 'vmail/login.html')



def username(request):
    text = []
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
            value = text.replace(' ', '')
            data_dict['username'] = value
            engine = pyttsx3.init()  # object creation
            rate = engine.getProperty('rate')  # getting details of current speaking rate
            print(rate)  # printing current voice rate
            engine.setProperty('rate', 200)  # setting up new voice rate
            volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
            print(volume)  # printing current volume level
            engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
            voices = engine.getProperty('voices')  # getting details of current voice
            engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
            engine.say(value)

            engine.runAndWait()
            engine.stop()
            return render(request, 'vmail/login.html', {'value': value})
        except:
            engine = pyttsx3.init()  # object creation
            rate = engine.getProperty('rate')  # getting details of current speaking rate
            print(rate)  # printing current voice rate
            engine.setProperty('rate', 125)  # setting up new voice rate
            volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
            print(volume)  # printing current volume level
            engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
            voices = engine.getProperty('voices')  # getting details of current voice
            engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
            engine.say('Could not recognize')
            engine.runAndWait()
            engine.stop()
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
            return render(request, 'vmail/login.html')
    print(text)
    return render(request, 'vmail/login.html',)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, template_name='vmail/login.html')


def login_user(request):
    # username1 = 'kbista.logispark@GMAIL.COM'
    # password1 = '#Bullet123!'
    # username1 = credit['username']
    # password1 = credit['password']
    # print(password1)
    # print(username1)

    print(data_dict['username'])
    print(data_dict['password'])
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            if (server.login(data_dict['username'], data_dict['password'])):
                engine = pyttsx3.init()  # object creation
                rate = engine.getProperty('rate')  # getting details of current speaking rate
                print(rate)  # printing current voice rate
                engine.setProperty('rate', 125)  # setting up new voice rate
                volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
                print(volume)  # printing current volume level
                engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
                voices = engine.getProperty('voices')  # getting details of current voice
                engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
                engine.say('You have been sucessfully logged in.')
                engine.runAndWait()
                engine.stop()
                return render(request, 'vmail/home.html')
            else:
                engine = pyttsx3.init()  # object creation
                rate = engine.getProperty('rate')  # getting details of current speaking rate
                print(rate)  # printing current voice rate
                engine.setProperty('rate', 125)  # setting up new voice rate
                volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
                print(volume)  # printing current volume level
                engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
                voices = engine.getProperty('voices')  # getting details of current voice
                engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
                engine.say('Invalid username or password. Try again')
                engine.runAndWait()
                engine.stop()
                return redirect('login')
    except:
        engine = pyttsx3.init()  # object creation
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        engine.setProperty('rate', 125)  # setting up new voice rate
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        engine.say('Invalid username or password. Try again')
        engine.runAndWait()
        engine.stop()
        return redirect('login')
