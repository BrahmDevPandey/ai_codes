# program to implement BFS of a directed graph
visited = []
graph = {
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','e'],
    'd':['b','f'],
    'e':['c','g'],
    'f':[],
    'g':['e','h'],
    'h':['g','i'],
    'i':['h','j'],
    'j':['i','k'],
    'k':['j','l'],
    'l':['k','m'],
    'm':[]
}

initial = 'a'
goal1 = 'f'
goal2 = 'm'

def bfs(visited, graph, node):
    queue = []
    queue.append(node)
    visited.append(node)
    
    while True:
        s = queue.pop(0)  #pop from the beginning        
        # now push all neighbours of s into queue
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
        if (goal1 in visited) or (goal2 in visited):
          print(visited)
          break

# driver code
bfs(visited, graph, initial)
