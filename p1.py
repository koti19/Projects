import random

target = random.randint(1, 1000)

while True:
    yourchoice = input("Guess the target or Quit(Q): ")

    if(yourchoice == "Q"):
        break
        
    yourchoice = int(yourchoice)

    
    if(yourchoice == target):
        print("CORRECT GUESS!!!")
        break
    elif(yourchoice < target):
        print("Your number is small. Take a bigger guess...")
    else:
        print("Your number is big. Take a smaller guess...")
    



print("-----GAME OVER!!!-----")
