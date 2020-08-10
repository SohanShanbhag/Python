import random
from random import choice
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
r = sr.Recognizer()
weapon = ""

weapons = ["rock", "paper", "scissors"]

computerChoice = weapons[random.randint(0, 2)]

#rate#
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)

#voice#
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print("Welcome To STARcade's ROCK PAPER SCISSORS GAME!!")
engine.say("Welcome To STARcade's ROCK PAPER SCISSORS GAME!!")
engine.say("Wear Headphones for a better microphone experience")
print("\nThe Rules are pretty simple : \n1. Tell me your weapon by speaking in the Microphone. \n2. I will give you my weapon and we will decide the winner.")
engine.say("\nThe Rules are pretty simple : \n Tell me your weapon by speaking in the Microphone. \nI will give you my weapon and we will decide the winner.")
engine.runAndWait()

def Fight():
    def Weapon():                                                                                      
        with sr.Microphone() as source:                                                                       
            print("\nGo ahead and tell me your weapon - \nI'm Listening.....")
            engine.say("\nGo ahead and tell me your weapon - \nI'm Listening.....")
            engine.runAndWait()
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            weapon = r.recognize_google(audio, language='en-in')
            print('Your Weapon : ' + weapon + '\n')
            engine.say('Your Weapon : ' + weapon + '\n')
            engine.runAndWait()
            
        except sr.UnknownValueError:
            engine.say('Sorry! I didn\'t get that! You might want to type the weapon')
            engine.runAndWait()
            
            weapon = str(input('Weapon: '))
            print("Your Weapon : " + weapon + "\n")

        return weapon

    weapon = Weapon()

    print("\nComputer's Weapon : " + str(computerChoice))
    engine.say("Computer's Weapon : " + str(computerChoice))
    engine.runAndWait()

    print("\nFIGHT - " + weapon + " V/s " + computerChoice)
    engine.say("FIGHT - " + weapon + " versus " + computerChoice)
    engine.runAndWait()

    if(weapon == "rock") and (computerChoice == "paper"):
        print("\nYou Lose! The Computer's " + computerChoice + " covers Your " + weapon)
        engine.say("\nYou Lose! The Computer's " + computerChoice + " covers your" + weapon)
        engine.runAndWait()

    elif(weapon == "paper") and (computerChoice == "rock"):
        print("\nYou Win! Your " + weapon + " covers the Computer's " + computerChoice)
        engine.say("\nYou Win! Your " + weapon + " covers the Computer's" + computerChoice)
        engine.runAndWait()

    elif(weapon == "paper") and (computerChoice == "scissors"):
        print("\nYou Lose! The Computer's pair of " + computerChoice + " cut your " + weapon)
        engine.say("\nYou Lose! The Computer's " + computerChoice + " cut your " + weapon)
        engine.runAndWait()

    elif(weapon == "scissors") and (computerChoice == "paper"):
        print("\nYou Win! Your pair of " + weapon + " cut the Computer's " + computerChoice)
        engine.say("\nYou Win! Your pair of" + weapon + " cuts the Computer's " + computerChoice)
        engine.runAndWait()

    elif(weapon == "scissors") and (computerChoice == "rock"):
        print("\nYou Lose! The Computer's " + computerChoice + " smashes your pair of " + weapon)
        engine.say("\nYou Lose! The Computer's " + computerChoice + " smashes your pair of " + weapon)
        engine.runAndWait()

    elif(weapon == "rock") and (computerChoice == "scissors"):
        print("\nYou Win! Your " + weapon + " smashes the Computer's " + computerChoice)
        engine.say("\nYou Win! Your " + weapon + " smashes the Computer's " + computerChoice)
        engine.runAndWait()

    elif(weapon == "paper") and (computerChoice == "paper"):
        print("It's a tie!!")
        engine.say("It's a tie")
        engine.runAndWait()

    elif(weapon == "rock") and (computerChoice == "rock"):
        print("It's a tie!!")
        engine.say("It's a tie")
        engine.runAndWait()

    elif(weapon == "scissors") and (computerChoice == "scissors"):
        print("It's a tie!!")
        engine.say("It's a tie")
        engine.runAndWait()

startGame = Fight()

while True:
    def getAnswer():                                                                                   
        with sr.Microphone() as source:
            print("Would you like to restart the game? : ")
            engine.say("Would you like to restart the game? : ")
            engine.runAndWait()
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            answer = r.recognize_google(audio, language='en-in')
            print('You Said : ' + answer + '\n')
            
        except sr.UnknownValueError:
            engine.say('Sorry sir! I didn\'t get that! You might want to type the command!')
            engine.runAndWait()
            
            answer = str(input('Your Answer [yes/no]: '))

        return answer

    answer = getAnswer()

    if("yes" in answer):
        print("Okay, restarting the game.....")
        engine.say("Okay, restarting the game.....")
        engine.runAndWait()
        computerChoice = weapons[random.randint(0, 2)] 
        Fight()

    if("now" in answer):
        print("Okay, Terminating Game. Goodbye!!")
        engine.say("Okay, Terminating Game. Goodbye!!")
        engine.runAndWait()
        exit(0)
