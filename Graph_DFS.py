#Depth first search 
#It starts somewhere- goes as deep as possible-got stuck- go back-try new path
#when u define a graph ->adjacency list- which shows the neighbours of every node

##By using Recursion :
graph={'A':['B','C'],'B':['D'],'C':[],'D':[]}
def dfs(graph,node,visited):
    print(node)
    visited.add(node)
    for neighbour in graph[node]:
        print("neighbours of node is "+neighbour)
        if neighbour not in visited:
            dfs(graph,neighbour,visited)

dfs(graph,'A',set())          
    
##By using Stack
def dfs_Stack(graph,start):
    visited=set()
    stack=[start]
    while stack:
        node=stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                print("neighbour the node is "+neighbour)
                stack.append(neighbour)

dfs_Stack(graph,'A')