#COPYRIGHT CyberFalcon101. Forks are allowed as long as the author is credited.
import random
#The words are here; don't look at them!
wordlist3 = ["ACE","ACT","ADD","AGE","AIR","ANT","ARM","ART","ASH", "BAG","BAN","BAT","BED","BEE","BIT","BOX","BUN","BUS","CAB","CAN","CAP","CAR","CAT","COW","CUP","DAY","DOG","DOT","EAR","EGG","END","EYE","FAN","FIG","FIN","FOG","FUN","GAP","HAT","HEN","ICE","INK","JAM","JET","JOB","JOY","KEY","KID","LAB","LAP","LAW","LEG","LID","LIP","LOG","MAN","MAP","MAT","MIX","MUD","NET","OIL","ONE","PAN","PEN","PET","PIN","PIT","POT","RAT","RED","RUG","RUN","SAD","SEA","SET","SIP","SKY","SON","SUN","TAG","TAP","TEA","TIN","TIP","TOP","TOY","TUB","USE","VAN","WAR","WAY","WEB","WIN","YAK","ZOO"]
wordlist4 = ["BARN","BELL","BOND","BOOK","CASH","CHEF","CITY","CLUB","COAT","CODE","COIN","CORN","CREW","DEED","DEER","DESK","DISH","DOOR","DUCK","DUST","FACE","FISH","FLAG","FOOD","GAME","GIFT","GOAL","GOLD","HAND","HILL","HOME","HOPE","KING","LAMB","LEAF","LION","MOON","NAME","NECK","NOSE","NOTE","OATH","PACK","PAGE","PAIN","PALM","PARK","PART","PATH","PEAR","PENY","PICK","PINE","PIPE","PLAN","PLUG","POEM","PORT","POST","PUMP","QUIZ","RACE","RAIL","RAIN","RANK","RATE","RING","ROAD","ROCK","ROLE","ROOT","ROPE","RULE","SALT","SAND","SEAT","SEED","SHIP","SHOP","SHOW","SIGN","SINK","SNOW","SOAP","SONG","SOUL","STAR","STEM","STEP","STOP","SUIT","TANK","TASK","TEAM","TENT","TEST","TIME","TOOL","TOUR","TREE","TRIP","USER","WALL","WAVE","WEEK","WIND","WOOD","WORD","WORK","YARD","ZONE"]
wordlist5 = ["APPLE","HOUSE","PIZZA","ROUND","GREEN","CHAIR","TABLE","LIGHT","MOUSE","PHONE","CLOUD","BRICK","WATER","PLANE","TRAIN","SHEET","SPOON","FORKS","DOORS","WHEEL","SNAKE","ZEBRA","TIGER","LIONS","BEARS","HORSE","SHEEP","GOOSE","BREAD","GRAPE","LEMON","MANGO","PEACH","BERRY","OLIVE","ONION","GARLIC","CANDY","SUGAR","SALAD","STEAK","BEANS","PASTA","CAKES","BRAIN","HEART","BONES","TEETH","SHOES","SOCKS","COATS","SCARF","GLOVE","WATCH","CLOCK","RADIO","TREES","GRASS","STARS","SKIES","RIVER","OCEAN","EARTH","STONE","FLAME","SMOKE","CYCLE","DRIVE","WINGS","COVER","STICK","ROCKS","NOISE","BAGEL","BULBS","CABLE","CAMEL","CANDY","CARGO","CHAIN","CHEST","CLOWN","COINS","CRANE","CROWN","DRESS","FENCE","FIELD","FLOOR","FRUIT","GAMES","GLASS","GLOBE","GUEST","HONEY","JELLY","METAL","MOTOR","PAPER","PILOT","PLANT","POWER","QUEEN","ROBOT"]
wordlist6 = ["BOTTLE", "BUTTON", "CANDLE", "CARPET", "DOCTOR", "FOLDER", "JACKET", "KITTEN", "MARKET", "NAPKIN", "OCEANS", "POCKET", "PUZZLE", "ROCKET", "TICKET", "WINDOW", "BANNER", "BREEZE", "CATTLE", "DOLLAR", "FIGURE", "FLOWER", "GARDEN", "HAMMER", "ISLAND", "JUNGLE", "LADDER", "LIZARD", "MARKER", "NATION", "OBJECT", "ORANGE", "PEBBLE", "PEOPLE", "PENCIL", "PRISON", "RIBBON", "SALMON", "SCHOOL", "SCREEN", "SILVER", "SPOONS", "STREET", "TABLET", "TUNNEL", "TROPHY", "ACORNS", "BOTTLE", "CARTON", "CIRCUS", "COFFEE", "COOKIE", "CROWNS", "DESERT", "DINNER", "DRAGON", "EAGLES", "ENGINE", "FENCES", "FRIDGE", "FRUITS", "GLOVES", "GRAPES", "HELMET", "HORSES", "HOTDOG", "LOCKER", "MARKET", "MIRROR","NEEDLE", "OFFICE", "PICKLE", "QUOTES", "RULERS", "SANDAL", "TOWELS"]
wordlist7 = ["BALLOON","BISCUIT","CABINET","CAPTAIN","CANYONS","CASHIER","CENTURY","CHICKEN","CITIZEN","CLIMATE","COMPASS","COTTAGE","CRAYONS","CRICKET","CUPCAKE","DIAMOND","EMERALD","EXPERTS","FACTORY","FANTASY","FEATHER","FERRIES","FISHING","FLIGHTS","FORESTS","FORTUNE","FOSSILS","GARAGES","GIRAFFE","GLASSES","HARVEST","HEALTHY","HOLIDAY","ICEBERG","INSECTS","JOURNAL","JUSTICE","KITCHEN","LANTERN","LAWYERS","LEAGUES","LIBRARY","LOCKERS","LOUNGES","MAILBOX","MANGOES","MEADOWS","MEDICAL","MESSAGE","MONSTER","MUSEUMS","NEEDLES","NETWORK","NUGGETS","OFFICER","OUTDOOR","PACKAGE","PANTHER","PASSAGE","PATTERN","PENGUIN","PHANTOM","PHRASES","PICTURE","PLANNER","PLASTIC","PRINTER","PROJECT","PYRAMID","RACCOON","RAILWAY","RECEIPT","REPTILE","SADDLES","SAILING","SAMPLES","SCANNER","SEASONS","SERVICE","SHADOWS","SHOVELS","SKATERS","SLOGANS","SNOWMAN"]
wordlist8 = ["AIRPLANE","BACKPACK","BASEBALL","BEDROOMS","BICYCLES","BOOKCASE","BUILDING","CAMPFIRE","CARTOONS","CHERRIES","CHICKENS","COCONUTS","COOKBOOK","CROSSING","CUCUMBER","DAFFODIL","DAYLIGHT","DIAMONDS","DOLPHINS","DOORSTEP","DRAWINGS","DUCKLING","EGGPLANT","ELEVATOR","ENVELOPE","EYEBROWS","FARMYARD","FESTIVAL","FLAMINGO","FOOTBALL","FOREHEAD","FREEWAYS","FRONTIER","GARDENER","GATEWAYS","GEMSTONE","GOLDFISH","HABITATS","HAMMOCKS","HANDBAGS","HARDWARE","HAYSTACK","HEADBAND","HIGHWAYS","HONEYBEE","ICECREAM","KEYBOARD","KITCHENS","LANTERNS","LOCKDOWN","MARKETED","MEDICINE","MESSAGES","MOUNTAIN","NECKLACE","NOTEBOOK","OFFICERS","OUTDOORS","PASSPORT","PATTERNS","PENGUINS","PICTURES","PRINTERS","PROJECTS","PYRAMIDS","RACCOONS","RAILWAYS","RECEIPTS","REPTILES"]
print('Welcome to Hangman...')
print('There are three modes you can choose from:')
print('1. Easy Mode: Maximum 20 guesses allowed.')
print('2. Medium Mode: Maximum 15 guesses allowed.')
print('3. Hard Mode: Maximum 10 guesses allowed.')
def funct():
    ask = input('Easy, medium or hard mode (e/m/h)? ').lower()
    if ask == 'e':
        def func():
            que = input('How much letters do you want the word to be (3,4,5,6,7,8)? ')
            if que == '3':    
                word = random.choice(wordlist3)
                guess = '***'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(3):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '4':    
                word = random.choice(wordlist4)
                guess = '****'
                for n in range(20):
                    if word!= guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(4):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '5':    
                word = random.choice(wordlist5)
                guess = '*****'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(5):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '6':    
                word = random.choice(wordlist6)
                guess = '******'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(6):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '7':    
                word = random.choice(wordlist7)
                guess = '*******'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(7):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '8':    
                word = random.choice(wordlist8)
                guess = '********'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(8):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            else:
                print('Invalid input.')
                func()
        func()
    elif ask == 'm':
        def func():
            que = input('How much letters do you want the word to be (3,4,5,6,7,8)? ')
            if que == '3':    
                word = random.choice(wordlist3)
                guess = '***'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(3):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '4':    
                word = random.choice(wordlist4)
                guess = '****'
                for n in range(15):
                    if word!= guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(4):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '5':    
                word = random.choice(wordlist5)
                guess = '*****'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(5):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '6':    
                word = random.choice(wordlist6)
                guess = '******'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(6):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '7':    
                word = random.choice(wordlist7)
                guess = '*******'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(7):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '8':    
                word = random.choice(wordlist8)
                guess = '********'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(8):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            else:
                print('Invalid input.')
                func()
        func()
    elif ask == 'h':
        def func():
            que = input('How much letters do you want the word to be (3,4,5,6,7,8)? ')
            if que == '3':    
                word = random.choice(wordlist3)
                guess = '***'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(3):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '4':    
                word = random.choice(wordlist4)
                guess = '****'
                for n in range(10):
                    if word!= guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(4):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '5':    
                word = random.choice(wordlist5)
                guess = '*****'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(5):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '6':    
                word = random.choice(wordlist6)
                guess = '******'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(6):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '7':    
                word = random.choice(wordlist7)
                guess = '*******'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(7):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '8':    
                word = random.choice(wordlist8)
                guess = '********'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(8):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            else:
                print('Invalid input.')
                func()
        func()
    else:
        print('Invalid input.')
        funct()
funct()
