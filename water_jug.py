# water jug problem
m = int(input("Enter capacity of first jug: "))
n = int(input("Enter capacity of second jug: "))

def findStep(x, y, rule):
    if rule == 1:
        x = m
    elif rule == 2:
        y = n
    elif rule == 3:
        x = 0
    elif rule == 4:
        y = 0
    elif rule == 5:
        t = n - y
        x = x - t
        y = n
    elif rule == 6:
        t = m - x
        y = y - t
        x = m
    elif rule == 7:
        y = min(y+x, n)
        x = 0
    elif rule == 8:
        x = min(x+y, m)
        y = 0
    else:
        print("Invalid rule")
    return x,y

x = 0
y = 0
c = int(input("Enter the volume needed to be measured: "))

while x != c and y != c:
    rule = int(input("Enter rule to use: "))
    x, y = findStep(x, y, rule)
    print(x,y)
