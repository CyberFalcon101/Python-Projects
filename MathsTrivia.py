import time 
score = 0
print('Welcome to Entertaining Maths Trivia With the Brainy Chatbot...')
time.sleep(2)
print('NOTE: In some instances, there may be a brief delay before the text appears (maximum of 5 seconds). This is expected behavior and does not indicate any issue with either the program or your device.')
time.sleep(3)
print('Loading...')
time.sleep(3)
print("Brainy Chatbot {brains in the metaphorical sense, of course, though the CHAT part in 'chatbot' is very literal indeed}: Ladies and gentlemen, boys and girls, WELCOME TO TODAY'S ABSOLUTELY THRILLING .... MATHS TRIVIA!!!")
time.sleep(5)
print("(Pause)")
time.sleep(1.5)
print("Brainy Chatbot{a little disappointedly}: No applause? Fine.")
time.sleep(2)
print("Brainy Chatbot, to the Audience: Anyway, I'm so delighted to tell you that, by random, we have chosen a person from the crowd to participate in our quiz today!!")
time.sleep(3.5)
print("Brainy Chatbot, to You: Hello there! Can we have your name, please?")
name = input("You: ")
print('Brainy Chatbot: Okay, ' + name + ". So, a few questions before we start. Are you excited for today's trivia (yes/no)?")
ans = input("You, to Brainy Chatbot: ").lower()
if ans == 'yes':
    print("Brainy Chatbot, to You: I'm so glad you are! Not much people are, to be honest. Quite sad, really. I'd shed a few tears if I could.")
elif ans == 'no':
    print("Brainy Chatbot, to You {in a whisper}: Well, I can't really take 'no' for an answer, can I?? I mean, there's people waiting out there! Who's gonna do it if you don't? C'mon, just say yes, can't you?! Please!!!")
    ans2 = input("You, to Brainy Chatbot: ").lower()
    if ans2 == 'yes':
        print('Brainy Chatbot: Why, thank you! Now, as the audience are waiting, I think we should start.')
    else:
        print("Brainy Chatbot, to You {still in a whisper}: Hmph. Ok. I'm not giving you a choice anymore. You're still gonna do it! Everyone's waiting for you!")
else:
    print("Brainy Chatbot, to You: Well, I dunno what you said, but I'm just gonna pretend I heard you say yes. So let's get on with the quiz! (And look at the bright side - I'm helping you get extra maths practice, right?!)")
time.sleep(2)
print("Brainy Chatbot, to You: First Q. What's 2483343483374863683 times 0? ")
first =input("You: ").lower()
if first == '0' or first == 'zero':
  print ("Brainy Chatbot, to You: Correct! The answer was 0. But it was a pretty easy question anyway, so don't go polishing your trophy yet! And anyway, we'll see how you'll go in the next Q.")
  score = 1
  time.sleep(3)
else:
  print('Brainy Chatbot, to You: Nooooo. The right answer is 0. Maybe you should try and listen a little harder during your maths classes.')
  time.sleep(1)
  print('Brainy Chatbot, to You: Next question.')
  time.sleep(0.5)
print("Brainy Chatbot, to You: ARE YOU READY?")
time.sleep(1.5)
print("Brainy Chatbot, to You: ARE YOU SET {whatever that means}?")
time.sleep(1.5)
print('Brainy Chatbot, to You: GO!!!!!!!!!!!!')
time.sleep(1.5)
print("Brainy Chatbot, to You: Well, maybe that wasn't as motivating as I thought...?")
time.sleep(2)
print("Brainy Chatbot, to You: Nevertheless. Second question. What's the square root of 144? ")
second = input("You: ").lower()
if second == '12' or second == 'twelve':
  print ('Brainy Chatbot{admits reluctantly:} Ok, ok, you got it right. Maybe you ARE smarter than I thought. But are you clever enough to ace the next question?')
  score = score + 1
else:
  print ("Brainy Chatbot, to You: Nope! Got it wrong. The right answer is 12. I hope you weren't chatting to your friends while your teacher explained this all to you...? Anyway. Prepare yourself for the absolutely gruelling questions that are coming next(just kidding!)")
time.sleep(3.5)
print('Brainy Chatbot, to You: Third question: What is 1000000000000 minus 1? ')
third = input("You: ")
if third == '999,999,999,999' or third == '999999999999':
  print("Brainy Chatbot, to You: Ok, yeah. You're right. The answer is 999999999999. Or 999,999,999,999. Whichever you like.")
  score = score + 1
  time.sleep(4)
else:
  print ("Brainy Chatbot, to You: That is incorrect. The right answer is 999999999999. Or 999,999,999,999. Well, it was admittedly a hard Q, so I'll let that pass. But don't think I'm still gonna give you a score!")
  time.sleep(4)
print("Brainy Chatbot, to You: Fourth question. This should be as easy as decrypting a SHA-256 hash ... what? You don't know what that is? Well, I'm not gonna do to details now, or this'll turn into a computing quiz.")
time.sleep(3)
print("Brainy Chatbot, to You: Anyway, here's the 4th Q. It's easy stuff. What's 75 + 25? ")
fourth = input('You: ').lower()
if fourth == '100' or fourth == 'hundred':
  print ("Brainy Chatbot, to You: Yeah, the answer's 100. No surprise you got it right.")
  score = score + 1
  time.sleep(1.5)
else:
  print ("Brainy Chatbot, to You: ...... Well. The answer is actually 100. It took me 0.33 nanoseconds to calculate that. That's 0.00000000033 seconds. But maybe I can't expect humans to be the same?")
  time.sleep(3)
print('Brainy Chatbot, to You: Fifth question- does 2 plus 2 give you the same answer as 2 times 2(yes/no)?')
fifth = input('You: ').lower()
if fifth == 'yes':
  print ("Brainy Chatbot, to You: That's right! They both give the answer 4. Wasn't that hard, eh?")
  time.sleep(2)
  score = score + 1
else:
  print ('Brainy Chatbot, to You: ....Well, not quite. They DO both give the answer of 4. What have you seriously been doing during class time?!')
  time.sleep(2)
print('Brainy Chatbot, to You: Sixth question- What is 123,456,789 divided by 0? ')
input("You: ")
print ("Brainy Chatbot, to You: Well, this is actually a trick question {hehehehe}. The answer's actually undefined.")
time.sleep(3)
print('Brainy Chatbot, to You: Seventh question: Maths riddle! I am an odd number. Take away a letter and I become even. What number am I? ')
seven = input("You: ").lower()
if seven == 'seven' or seven == '7':
      print ("Brainy Chatbot, to You: Hey!! How did you know?? Did you search it up on the internet?! Ok, ok. You got it right (somehow). It's seven. Coz Seven minus S = Even. {FINE. I know that wasn't a maths Q... but it's still related to maths, isn't it?}")
      time.sleep(4)
      score = score + 1
else:
  print ("Brainy Chatbot, to You: Nah! Incorrect. The right answer's seven, coz Seven minus S = Even. Got it? {Ok, ok, I know that wasn't a maths Q... but it's still related to maths, isn't it??}")
  time.sleep(3)
print("Brainy Chatbot, to Audience: Anyway, I suppose that's it for the day. And for our friend " + name + " here, may we have a round of applause!")
time.sleep(3)
print ('Brainy Chatbot, to You: Good job! Your score is', score, "out of 6 (yeah, 6, not 7. Remember one of the questions was a trick Q? {hehe})")
time.sleep(3)
print('Brainy Chatbot, to You: Anyway, see you next time! All of you!')
time.sleep(3)
print("I hope you enjoyed this program!")
