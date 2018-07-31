#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 8
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
name = [{"player":"","choise":""} for player in range(2)]
stillWantToPlay = 'y'
for player in range(2):
    name[player]["player"] = raw_input("Player %d please enter your name\n" % int(player+1))

while(stillWantToPlay == 'y'):
    for player in range(2):
        while name[player]["choise"] != 'rock' and \
                name[player]["choise"] != 'paper' and \
                name[player]["choise"] != 'scissors':
            name[player]["choise"] = raw_input("%s please choose Rock-Paper-Scissors\n" % name[player]["player"]).lower()

    if(name[0]["choise"] == 'rock' and name[1]["choise"] == 'paper'):
        print("congratulations to the winner - %s" % name[1]["player"])
    elif(name[0]["choise"] == 'rock' and name[1]["choise"] == 'scissors'):
        print("congratulations to the winner - %s" % name[0]["player"])
    elif(name[0]["choise"] == name[1]["choise"]):
        print("Teko!! Play again")
    elif(name[0]["choise"] == 'paper' and name[1]["choise"] == 'rock'):
        print("congratulations to the winner - %s" % name[0]["player"])
    elif(name[0]["choise"] == 'paper' and name[1]["choise"] == 'scissors'):
        print("congratulations to the winner - %s" % name[1]["player"])
    elif(name[0]["choise"] == 'scissors' and name[1]["choise"] == 'rock'):
        print("congratulations to the winner - %s" % name[1]["player"])
    else:
        print("congratulations to the winner - %s" % name[0]["player"])

    name[0]["choise"] = ""
    name[1]["choise"] = ""
    stillWantToPlay = raw_input("Want to play again? Y/N\n").lower()
