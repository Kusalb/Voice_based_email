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
from vmail.models import Compose, Inbox, Draft

data_dict = {}


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

    value = text.replace(' ', '')
    print(text)
    data_dict['recipent'] = value
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
    message = Compose.objects.create(to=data_dict['recipent'], subject=data_dict['subject'], message=data_dict['message'])
    message.save
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "kbista.logispark@gmail.com "
    receiver_email = to
    password = '#Bullet123!'
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
    sub = data_dict['subject']
    to = data_dict['recipent']
    msg = data_dict['message']
    print(sub)
    print(to)
    print(msg)
    msgobject = Draft.objects.create(to=data_dict['recipent'], subject=data_dict['subject'], message=data_dict['message'])
    msgobject.save
    return render(request, 'vmail/home.html')


def compose(request):
    return render(request, 'vmail/compose.html')


def inbox(request):
    username = 'kbista.logispark@gmail.com'
    password = '#Bullet123!'
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
        counter = counter +1
        print(counter)
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
    return render(request, 'vmail/inbox.html', {'inbox': inbox_message})


def outbox(request):
    outbox = Compose.objects.all()
    return render(request, 'vmail/outbox.html', {'outbox': outbox})


def draft(request):
    draft = Draft.objects.all()
    return render(request, 'vmail/draft.html', {'draft': draft})



def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, template_name='vmail/login.html')

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(username)
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            if(server.login(username, password)):
                return render(request, 'vmail/home.html')
            else:
                return render(request, 'vmail/login.html')
    except:
        return render(request, 'vmail/login.html')




