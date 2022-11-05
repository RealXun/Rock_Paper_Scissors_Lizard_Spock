# Rock Paper Scissors Spock Lizard
Rock Paper Scissors Lizard Spock is an extension of the classic game of chance, Rock Paper Scissors, created by Sam Kass and Karen Bryla

<p align="center">
    <img src="https://github.com/RealXun/Paper_Rock_Scissors_Spock_Lizard/blob/main/Resources/Cover.png"alt="drawing" width="300">

## Updates

Rock_Paper_Scissors_Lizard_Spock_V2 now contains:
- def user_choose
- def machine_choose

## Objectives
1. Loop Usage
2. Data capture by console
3. Use if-elif-else
4. Use of try-except
5. Definition of functions. Modular programming.
6. Logical operators.
7. Print by console
8. Import of external modules
  
### Requirements 
- Import the choice function from the random module.
- Defines a function that asks for an odd number by keyboard, until it is not valid will keep asking.
- Assign the 5 possible options to a list.
- Assign a variable to the maximum number of games: 1, 3, 5, etc...
- This time the previously defined function is used
- Assign a variable to the number of games a player must win to win. Preferably the value will be based on the number of maximum games.
- Define a function that randomly returns one of the 5 options. This will correspond to the play of the machine. Totally random.
- Define a function that asks for your choice among the 5 must only allow one of the 5 options. This is defensive programming. If it is not valid, keep asking until it is.
- Define a function that resolves a combat.
- Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins.
- Define a function that shows the choice of each player and the state of the game
- This function must be used every time the accumulated points are updated
- Create two variables that accumulate the games won by each participant
- Create a loop that iterates as long as no player reaches the win minimum necessary to win. Inside the loop resolve the move of the machine and asks the player's.
- Compare them and update the value of the variables
- Accumulate the games won by each participant.
- Announce by console the winner of the game based on who has the most wins accumulated.
