# program to implement BFS of a directed graph
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

def bfs(visited, graph, node):
    queue = []
    queue.append(node)
    visited.append(node)
    
    print("The Breadth First Traversal (BFS) of the given graph staring from", node, "is:")
    while queue:
        s = queue.pop(0)  #pop from the beginning
        print(s, end=" ")
        
        # now push all neighbours of s into queue
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

# driver code
bfs(visited, graph, 'A')