##In recursion, a function pauses at the recursive call, and continues after the recursive call finishes.
#Recursion execution order is reversed.
#We go down first, then calculate while coming back.
#Going down → recursive calls
#Coming up → actual answers
def open_doll(n):
    if n==1:
        print("reached smallest doll")
        return
    print("opening doll is ",n)
    open_doll(n-1)
    print("closing doll is ",n)
open_doll(5)

def open_russiandoll(n):
    if n==1:
        print("smallest doll is opened")
    else:
        print("opening russian doll is ",n)
        open_russiandoll(n-1)
        print("closing dolll is ",n)
open_russiandoll(5)

##Tower of Hanoi
def hanoi(n,source,helper,destination):
    if n==1:
        print("move disk 1 from ",source,"to",destination)
    else:
        hanoi(n-1,source,destination,helper)
        print("move disk ", n ,"FROM ",source,"to", destination)
        hanoi(n-1,helper,source,destination)
hanoi(3,'A','B','C')

        

