from colors import bcolors

def hand(no):
    hands = {
        "1": ("Rock", """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""),
        "2": ("Paper", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""),
        "3": ("Scissor", """
   _    _
  (_)  / )
    | (_/ 
   _+/  
  //||
 // | )
(/  |/
"""),
        "4": ("Lizard", """
                       )/_
             _.--..---"-,--o_
        \L..'           ._O__)_
,-.     _.+  _  \..--( /
  `\.-''__.-' \ (     \_
    `'''       `\__   /|
                ')
"""),
        "5": ("Spock", """
     _______
---'    ____)____
           ______)
          _______)
         (______
         _______)
---.__________)
""")
    }
    return hands[no]



def print_hand(hand_name, ascii_art):
    print(hand_name)
    print(ascii_art)



def judge_winner(ai, user):
    ai_hand, ai_ascii_art = hand(ai)
    user_hand, user_ascii_art = hand(user)

    print("AI:")
    print_hand(ai_hand, ai_ascii_art)
    print("User:")
    print_hand(user_hand, user_ascii_art)
    
    if user == ai:
        print(bcolors.YELLOW + " It's a tie\n" + bcolors.DEFAULT)
        return "Tie"
    elif user == "3":
        if ai == "2" or ai == "4":
            print(bcolors.GREEN + " You won\n" + bcolors.DEFAULT)
            return "Win"
        else:
            print(bcolors.RED + " You lose\n" + bcolors.DEFAULT)
            return "Lose"
    elif user == "1":
        if ai == "3" or ai == "4":
            print(bcolors.GREEN + " You won\n" + bcolors.DEFAULT)
            return "Win"
        else:
            print(bcolors.RED + " You lose\n" + bcolors.DEFAULT)
            return "Lose"
    elif user == "2":
        if ai == "1" or ai == "5":
            print(bcolors.GREEN + " You won\n" + bcolors.DEFAULT)
            return "Win"
        else:
            print(bcolors.RED + " You lose\n" + bcolors.DEFAULT)
            return "Lose"
    elif user == "4":
        if ai == "5" or ai == "2":
            print(bcolors.GREEN + " You won\n" + bcolors.DEFAULT)
            return "Win"
        else:
            print(bcolors.RED + " You lose\n" + bcolors.DEFAULT)
            return "Lose"
    elif user == "5":
        if ai == "3" or ai == "1":
            print(bcolors.GREEN + " You won\n" + bcolors.DEFAULT)
            return "Win"
        else:
            print(bcolors.RED + " You lose\n" + bcolors.DEFAULT)
            return "Lose"
    else:
        print("Error")
        return "Error"