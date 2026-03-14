import random

#player takes only 1 stick
def nim_minimal(n):
    return 1

#random computer player
def nim(n):
    return random.choice(range(1,min(n,3)+1))

#optimal computer player 
def nim_best(n):
    taken=n%4
    if taken:
        return taken
    else:
        return random.choice(range(1,min(n,3)+1))
    
#human player 
def nim_human(n):
    while True:
        taken=int(input("These are %d sticks.How many do you take ?(1/2/3):  "%n))
        if taken in range(1,min(n,3)+1):
            return taken
        print("Illegal move ")

#List of all 4 player (player candiadates)--list of functions are stored here
player_pool=[nim_minimal,nim,nim_best,nim_human]
#convert list of functions to dictionary --every function has a name property
#  so based on that we will create a dictinary here so that we can call a function by using its name directly
player_pool={p.__name__:p for p in player_pool}
print("player pool after converting into dict")
#player selection 
#join combines strings with a separatoe
def select_players():
    players=[]
    while len(players)<2:
        print("These are the players :","/".join(player_pool.keys()))
        p=input("Enter a player: ")
        if p not in player_pool.keys():
            print("not  a valid player ")
            continue
        players.append(p)
    print("player %s begins,player %s playes second." %tuple(players))
    return players
#Game Controller
def game():
    while True:
        n=int(input("Enter Heap size "))
        if n>0:
            break
    current ,other=tuple(select_players())
    while n>0:
        print("Heap has  %d sticks " %n)
        taken=player_pool[current](n)
        print("%s takes %d sticks .\n"%(current,taken))
        n-=taken
        current,other=other,current
    print("%s has lost. "% current)

game()

