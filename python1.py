import random
def get_choices():
    player_choice=input("enter a choice (rock,paper,scissiors:)")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"comp":computer_choice}
    return choices

def check_win(player,computer):
    print("Player chose "+player+",computer chose "+computer)
    print(f"palyers chocie is {player},computer chose {computer}")
    if player==computer:
        return "its a tie"
    elif player=="rock":
        if computer=="scissors":
            return"rock hits the scissors! You won"
        else:
            return "Paper covers the rock!You lose"
    elif player=="paper":
        if computer=="rock":
            return"Paper covers the rock !You win"
        else:
            return"scissors cut the paper !You lose"
    elif player=="scissors":
        if computer=="paper":
            return "scissors cut the paper !You win"
        else:
            return "rock hits the scissors !You lose"
        
        
choices=get_choices()
player=choices["player"]
computer=choices["comp"]
print(check_win(player,computer))






