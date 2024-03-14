# Scissors cuts paper           S  > P
# Scissors decapitates lizard   S  > L
# Paper covers rock             P  > R
# Paper disproves Spock         P  > SP
# Rock crushes lizard           R  > L
# Rock crushes scissors         R  > S
# Lizard poisons Spock          L  > SP
# Lizard eats paper             L  > P
# SPock smashes scissors        SP > S
# SPock vaporizes rock          SP > R


import random 
import os
os.system("cls")
from colors import bcolors
from RPSfunk import judge_winner, print_hand
from msvcrt import getwch

print("""
1 = (R)ock
2 = (P)aper
3 = (S)cissor
4 = (L)izard
5 = (SP)ock
q = Quit
""")

times_played = 0
wins = 0
losses = 0
ties = 0

while True:
    times_played += 1
    print("Enter a number: ")
    user = getwch()
    ai = str(random.randint(1, 5))
    if user == "q":
        print("GG WP")
        print(bcolors.DEFAULT , ("resultat:  ") , bcolors.GREEN , "Wins: " , wins , bcolors.RED , " Losses: " , losses , bcolors.YELLOW , " Ties: " , ties , bcolors.DEFAULT)
        break
    else:
        result = judge_winner(ai, user)
        if result == "Win":
            wins += 1
        elif result == "Lose":
            losses += 1
        elif result == "Tie":
            ties += 1

    print(f"You have played {times_played} rounds")
    print(bcolors.GREEN , "Wins: " , wins , bcolors.RED , " Losses: " , losses , bcolors.YELLOW , " Ties: " , ties , bcolors.DEFAULT)