import random as r
import time as t
from pyfiglet import Figlet



def inputFunction():
    print("Please select one of the following[0-2]...")
    t.sleep(1)
    print("0. Rock\n1. Paper\n2. Scisscor")
    userInput  =  input("Input: ")
    return userInput


def stringValidator(input):
    
    if input == "0" or input == "1" or input == "2":
        return input
    
    else:
        
        thirdcounter = 0
        while thirdcounter !=1:
            input = inputFunction()   
            if input == "0" or input == "1" or input == "2":
                thirdcounter = 1
                return input
        

def isEmpty(input):
     secondCounter = 0
     if input == "":        
        while secondCounter !=1:
            input = inputFunction()        
            if input != "":
                secondCounter = 1
                return input
     else:
         return input


    
   

choice = ["Rock","Paper","Scissors"]
choiceNumber =  r.randint(0,2)
counter = 0
total = 3
custom_fig = Figlet(font='banner3-D')




print(custom_fig.renderText('WELCOME'))
t.sleep(3)
print("To our game of Rock Paper Scisscors!")
print("----------------------------------------")
t.sleep(3)
print(" ")





while(counter < total):
    print("Please select one of the following[0-2]...")
    t.sleep(3)
    print("0. Rock\n1. Paper\n2. Scisscor")


    stringInput = input("Input: ")
    

    stringNotEmpty = isEmpty(stringInput)

    validString = stringValidator(stringNotEmpty)

    userInput = int(validString)

    
    

    userPick =  choice[userInput]
           
    print("You have picked: " + userPick)


    t.sleep(3)

    print("The AI chooses...")

    t.sleep(3)

    print("calculating...")

    t.sleep(3)

    print("calculating...")

    t.sleep(3)

    print("calculating...")

    print(" ")

    print(choice[choiceNumber])



    if(userInput == 0 ):

        if (choiceNumber==0):
            t.sleep(1)     
            print(" ") 
            print("ITS A TIE!")
            counter = counter + 1
            t.sleep(1)
            print(" ")
            print(f"You have {total-counter} more tries")


        elif(choiceNumber==1):
            t.sleep(1)   
            print(" ")
            print(custom_fig.renderText("YOU LOSE!"))
            counter = counter + 1
            t.sleep(1)
            print(" ")
            print(f"You have {total-counter} more tries")
            
        else:
            t.sleep(1)
            print(" ") 
            print(custom_fig.renderText("YOU WIN!"))
            counter = 3


    elif(userInput == 1):
        if (choiceNumber==0):
            t.sleep(1)
            print(" ")   
            print(custom_fig.renderText("YOU WIN!"))
            counter = 3

        elif(choiceNumber==1):
            t.sleep(1)
            print(" ") 
            print("ITS A TIE!")
            counter = counter + 1
            print(f"You have {total-counter} more tries")
            
        else:
            t.sleep(1)
            print(" ") 
            print(custom_fig.renderText("YOU LOSE!"))
            counter = counter + 1
            t.sleep(1)
            print(" ")
            print(f"You have {total-counter} more tries")



    elif(userInput == 2):
        if (choiceNumber==0):
            t.sleep(1) 
            print(" ")  
            print(custom_fig.renderText("YOU LOSE!"))
            counter = counter + 1
            t.sleep(1)
            print(" ")
            print(f"You have {total-counter} more tries")

        elif(choiceNumber==1):
            t.sleep(1) 
            print(" ") 
            print(custom_fig.renderText("YOU WIN!"))
            counter = 3
            
        else:
            t.sleep(1) 
            print(" ")
            print("ITS A TIE!")
            counter = counter + 1
            t.sleep(1)
            print(" ")
            print(f"You have {total-counter} more tries")

    



    
















