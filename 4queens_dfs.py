# program to implement DFS of 4 Queens problem
visited = []
graph = {
    'a':['b','c','d','e'],
    'b':['f','g'],
    'c':['h'],
    'd':['i'],
    'e':['j','k'],
    'f':[], # dead state
    'g':['l'],
    'h':['m'],
    'i':['n'],
    'j':['o'],
    'k':[], # dead state
    'l':[], # dead state
    'm':['p'],
    'n':['q'],
    'o':[], # dead state
    'p':[], # final state
    'q':[]  # final state
}

initial = 'a'
goal1 = 'p'
goal2 = 'q'

def bfs(visited, graph, node):
    stack = []
    stack.append(node)
    visited.append(node)

    while True:
        s = stack.pop(-1)  #pop from the end
        # now push all neighbours of s into stack
        for neighbour in graph[s]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.append(neighbour)
        if (goal1 in visited) or (goal2 in visited):
          print(visited)
          break

# driver code
bfs(visited, graph, initial)
