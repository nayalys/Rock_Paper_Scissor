list = ["rock", "paper","scissors"]
import random

while True:
    while True: 
        user =  input ("Enter  Rock, Paper or Scissors:")
        lower = user.lower()

        if lower in list:
            print (f"User Selection:{lower} ") 
            break 
        else:
            print ("Invalid choice, please enter the correct word")
   
    comp_choice = random.choice(list)
    print (f"Computer Selection: {comp_choice}") 

    if (lower == comp_choice):
        print ("Game Tie")
    elif (lower == "scissors" and comp_choice == "paper"):
        print ( " scissors beat paper, the user is the winner")
    elif (lower == "scissors" and comp_choice == "rock"):
        print ( " Rock beat Scissors, computer is the winner")
    elif (lower == "rock" and comp_choice == "paper"):  
        print ( " Paper beat Rock, computer is the  winner")
    elif (lower == "rock" and comp_choice == "scissors"): 
        print ( " Rock beat Scissors, the user is the  winner")
    elif (lower == "paper" and comp_choice == "scissors"):  
        print ( " Scissors beat Paper, the user computer is the  winner")
    elif (lower == "paper" and comp_choice == "rock"):  
        print ( " Paper beat Rock, the user is the  winner")    
 
    resp = [ "yes","no"]
    while True:

        option = input ("\n Do you want to play again?: (yes/no):")
        option_lower = option.lower()
        
        if option_lower in resp:
             break
        else:
            print("Error, write Yes or No")
    
    if option_lower == "no":
        print ("Thanks for the Game")
        break

        
  
        
                                                                                