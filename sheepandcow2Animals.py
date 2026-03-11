start_stable=['C','C','E','S','S']
goal_state=['S','S','E','C','C']
def successors(stable):
    empty=stable.index('E')
    candidates=[empty+1,empty-1,empty+2,empty-2]
    candidates=[cd for cd in candidates if cd>=0 and cd<len(stable)]
    candidates=[cd for cd in candidates 
                if stable[cd:cd+2]==['C','E'] or
                  stable[cd-1:cd+1]==['E','S'] or 
                  stable[cd:cd+3]==['C','S','E'] or 
                  stable[cd-2:cd+1]==['E','C','S']]
    for cd in candidates:
        new_stable=stable[:] #copying original list
        new_stable[cd],new_stable[empty]=new_stable[empty],new_stable[cd]
        yield new_stable


def solution(stable,visited):
    if stable==goal_state:
        return [stable]
    visited.add(tuple(stable))
    for newstable in successors(stable):
        if tuple(newstable) not in visited:
            print(f"new stablle is  {newstable}")
            sol=solution(newstable,visited)
            print(f"sol i got in here is {sol}")
            if sol:
                return[stable]+sol
    return None

soln=solution(start_stable,set())
for s in soln:
    print(s)
    

## so what i am doing is i look for valid movements based on the empty space -which gives me some valid movements 
# which in branches gets dfs executed until if any branch reaches the final goal
##dfs goes deep down first and then builds path while coming up-- (path gets build backwards in deep recursion)--which is why soln gets to added the previous stable 