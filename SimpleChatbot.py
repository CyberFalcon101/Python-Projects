#COPYRIGHT CyberFalcon101. Forks are allowed as long as the author is credited. 
print('Welcome to Simple Chatbot...')
import time 
time.sleep(2)
print('Loading...')
time.sleep(3)
import random
questions = [
'Hi there, who are you? ',
"G'day, who are you? ",
"Who are you? ",
"What's your name? ",
"Hello, what's your name? ",
"Hi, what's your name? ",
]
name = input(random.choice(questions))
ans = input('Do you have a nickname(yes/no)? ').lower()
if ans == 'yes':
  nickname = input('What is your nickname? ')
  print ('Nice to have acquainted with you, ' + nickname + '!')
else:
  nickname = name + ' ' + name 
  print ("Then I'll call you " + nickname + '.')
input("How about we spend time with a few questions? ")
print('Alright then!')
hair = input('Tell me your descriptions. What colour hair do you have, ' + nickname + '? ').lower()
if 'black' in hair:
  print ('Black is one of the most common hair colour in the world.')
if 'brown' in hair:
  print ('Did you know that brown haired people are called brunettes?')
if 'blonde' in hair:
  print ('Blonde is a very nice colour!')
if 'yellow' in hair:
  print ('Yellow is a very nice colour!')
if 'red' in hair:
  print ('Red hair is very rare!')
if 'grey' in hair:
  print ("Okay!")
if 'white' in hair:
    print ('White hair is the colour of snow!')
eyes = input("What's the colour of your eyes? ")
if 'brown' in eyes:
  print ('Did you know that some brown eyes used to be originally blue?')
if 'grey' in eyes:
    print ('Did you know many babies are born with either grey or blue eyes?')
if 'gray' in eyes:
  print ('Did you know many babies are born with either grey or blue eyes?')
if 'green' in eyes:
    print ('Nice! Green eyes are the rarest of eye colours!')
if 'blue' in eyes:
    print ('Did you know many babies are born with blue eyes?')
if 'black' in eyes:
  print ("Black eyes aren't considered as a proper eye colour; rather they're dark.")
height = input('Are you very tall, tall, average, short or very short? ').lower()
if 'very short' in height:
  print ("Don't feel bad, being short isn't bad all the time!")
if 'short' in height:
  print ("Don't feel bad, being short isn't bad all the time!")
if'average' in height:
  print ("So neither tall nor short, eh?")
if 'tall' in height:
  print ("It's nice being tall!")
if  'very tall' in height:
  print ("Did you know the tallest man on Earth was 272cm long?")
colour = input('What is your favourite colour? ').lower()
if 'red' in colour:
  print ('Red is a very nice colour!')
if 'yellow' in colour:
  print ('Did you know that both orange and yellow symbolises happiness?')
if 'green' in colour:
    print ('Did you know green symbolises nature?')
if 'blue' in colour:
  print ('Did you know blue symbolises calmness?')
if 'purple' in colour:
  print ('Did you know purple symbolises royalty?')
if 'indigo' in colour:
  print ('Did you know indigo symbolises royalty?')
if 'orange' in colour:
  print ('Did you know both orange and yellow symbolises happiness?')
if 'black' in colour:
  print ('Did you know black symbolises mystery?')
if 'grey' in colour:
  print ('Did you know grey symbolises mood?')
if 'gray' in colour:
  print ('Did you know grey symbolises mood?')
if 'pink' in colour:
  print ('Did you know pink symbolises compassion?')
if 'white' in colour:
  print ('Did you know white symbolises innocence?')
print ('So you have ' + hair + ' hair, ' + eyes + ' eyes, your favourite colour is ' + colour + " and you're " + height + '.')
goodbyes = [
  'See ya later, ' + nickname + '!',
  "It's been nice talking to you, " + nickname + ", so I hope we chat again! See you!",
  "I'm going to go now, " + nickname + ", so goodbye!",
  "Goodbye " + nickname + "! It's been nice chatting with you.",
  "See you later, alligator!",
  "It's getting late now, I gotta go! Goodbye, " + nickname + "!",
]
print(random.choice(goodbyes))
