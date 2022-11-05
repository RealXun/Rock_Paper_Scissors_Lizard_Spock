#Defne conditions to use later.
# Number is odd
# Number is equal or greater than 3

def is_odd(first_input):
    if first_input % 2 != 0:
        return True
    else:
        False
        
def is_more_or_equal_1(first_input):
    if first_input >= 1:
        return True
    else:
        return False

#We start and infinite while
print("""How to Play Rock, Paper, Scissors, Lizard, Spock:

         Rock smashes scissors, and rock smashes lizard.
         Paper covers rock, and paper disproves Spock.
         Scissors cuts paper, and also decapitates (cuts the head off of) lizard.
         Lizard eats paper and poisons Spock.
         Spock vaporizes rock. Second, Spock smashes scissors.
    """)
while 1:
    first_input = int(input("Write the MAXIMUN number of rounds you wanna play:")) #The maximun numbers of rounds we are gonna play should be decided
    if is_odd(first_input) and is_more_or_equal_1(first_input): # Here we tell it umber is odd and Number is equal or greater than 3, correct, lets play
        print("\nInput taken successfully.","Number is odd and equal or greater than one.","The game starts now:")
        max_rounds = first_input # we rename the firs input to max_rounds
        played = 0 #number of played games
        machine_win = 0 #number of rounds the machine wins
        users_win = 0 #number of rounds the user wins
        to_win = int((max_rounds/2)+0.5) #Calculate the number of wins to win, if max_rounds is 5, if player/machine gets 3 winning rounds before the last round, player/machine wins
        games_left  = max_rounds-1 #How many rounds left
        
        while played < max_rounds:
            import sys #this will be used to end a loop when reached the max_rounds that were wanted to be played
            import random
            # Computer chooses randomly any number
            # among 1 , 2 and 3. Using randint method of random module
            random = random.randint(0, 4) #randomly returns one of the 3 options for the machines
           
            print("\nHere are the options:\n1)rock","\n2)paper","\n3)scissors","\n4)spock","\n5)lizard")
            if random == 0:
                machine = "rock"
            elif random == 1:
                machine = "paper"
            elif random == 2:
                machine = "scissors"
            elif random == 3:
                machine = "spock"
            elif random == 4:
                machine = "lizard"
            
            option = int(input("\nWrite the number of what you wanna use.:"))
            
            while option > 5 or option==0: #When player choose an option it should be 1, 2 or 3, if not it gives a message to pick again
                print("Incorrect option.")# pick again
            
            # initialize value of user variable
            # corresponding to the option value 
            if option == 1:
                user = "rock"
            elif option == 2:
                user = "paper"
            elif option == 3:
                user = "scissors"
            elif option == 4:
                user = "spock"
            elif option == 5:
                user = "lizard"
            
            #Here I show what user and machine did choose
            print("\nYou choose: ", user)
            print("The machine has chosen: ", machine)
            
            #The winning decision making. In the if it goes what the user can win. elif tie, else is what the user cannot win.
            if (machine == "rock" and user =="paper") or (machine == "paper" and user == "scissors") or (machine == "scissors" and user == "rock") or (machine == "lizard" and user == "rock") or (machine == "spock" and user == "paper"):
                users_win+=1
            elif (machine == "rock" and user =="spock") or (machine == "paper" and user == "lizard") or (machine == "scissors" and user == "spock") or (machine == "lizard" and user == "scissors") or (machine == "spock" and user == "lizard"):
                users_win+=1
            elif machine == user:
                print("\nTIE!!!")
            else:
                machine_win+=1 

            #We say how many rounds left, and many wins the player and the machine got so far in each round  
            print("\nJust",games_left,"game left to play","\nPlayer won",users_win ,"games","\nThe machine won",machine_win ,"games\n")               
            played+=1
            games_left-=1

            #Here if the user or machine won the minimun round to win (it change depending on the number or rounds) then the game stops
            if users_win==to_win or machine_win==to_win:
                    break
        
        if users_win<machine_win or machine_win==to_win:
            print("The machine is the winner!!!! Machine did win ",machine_win ,"games")
        elif users_win==to_win or machine_win<users_win:
            print("User is the winner!!!! User did win ",users_win ,"games")           
        else:
            print("There are no winners, TIE!!!!")

        #I have put it so that the infinite loop ends when reaching the number of games that were wanted to be played
        sys.exit() 
    else:
        if not is_odd(first_input) or is_more_or_equal_3(first_input): # Here we tell it number isnot odd and Number is not equal or greater than 1, so incorrect. Pick again
            print("Failed! The number of games must be odd and equal or greater than or equal to 1")
            continue #with it we go back to pick a number of rounds