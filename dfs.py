# program to implement DFS of a directed graph
visited = []
graph = {
    'A':['B', 'C'],
    'B':['D'],
    'C':['H'],
    'D':['E', 'F'],
    'E':['C', 'G'],
    'F':['G', 'H'],
    'G':['I'],
    'H':['A','G','I'],
    'I':[]
}

def dfs(visited, graph, node):
    queue = []
    queue.append(node)
    visited.append(node)
    
    print("The Depth First Traversal (DFS) of the given graph staring from", node, "is:")
    while queue:
        s = queue.pop(len(queue) - 1)  #pop from the ending
        print(s, end=" ")
        
        # now push all neighbours of s into queue
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

# driver code
dfs(visited, graph, 'A')