#candidates are ppl on boat side
def select_travellers(candidates):
    #You are selecting travellers to send on boat and u can send 1 or 2 travellers at a time so we have 2 cases here
    #one traveller
    for first in range(len(candidates)):
        yield [candidates[first]]

    #for 2 travellers
    for first in range(len(candidates)):
        for second in range(first+1,len(candidates)):
            yield [candidates[first],candidates[second]]

other_side={"left":"right","right":"left"}


#We need to check if the state is safe or not based on the rule 
#that is a sidekick should not be with any hero other than his own hero on any side of the river -which is dangerous for him
# so here we check if any kick is left alone with other heros on left and right sides

def safe(state):
    #unpacking my state tuple to fetch details of the persons
    person_pos,_=state
    #i am iterating over 2 sides to check bothe sides of the river for evry state
    for side in ['left','right']:
        #i am checking the side of kick and his hero and fetching index of kicks if left alone in the below list
        lone_kick=[index for (person,index) in person_pos 
                   if person=='kick' 
                   if person_pos[person,index]==side
                   if person_pos['hero',index]!=side]
        #I am collecting index of the heros present on the current side
        Other_hero=[index for (person,index)in person_pos
                      if person=='hero'
                      if person_pos[person,index]==side]
    if lone_kick and Other_hero:
        return False
    return True

##Succesor function (possible moves from a particualr state)


        


