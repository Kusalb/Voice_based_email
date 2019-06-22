# import pyttsx3
#
# data = 'value for js'
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
# engine.say(data)
# engine.say("Single left click to compose a mail.")
# # engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()
#

# import imaplib, ssl
# # username = request.POST.get('username')
# # password = request.POST.get('password')
# import smtplib
#
#
# username = 'kbista.logispark@gmail.com'
# password = '#Bullet123!'
# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# context = ssl.create_default_context()
# try:
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.ehlo()  # Can be omitted
#         server.starttls(context=context)
#         server.ehlo()  # Can be omitted
#         if(server.login(username, password)):
#             print('Sucessfully logged in')
# except:
#     print('try again')


mylist = [1, 2, 3, 4, 5]
mylist.reverse()

print(mylist)