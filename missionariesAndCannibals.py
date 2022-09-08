# missionaries and cannibals problem
m1 = 3
c1 = 3
m2 = 0
c2 = 0

def printState():
    print("Bank 1\t Bank 2")
    print("M C\t M C")
    print(m1, c1, "\t", m2, c2, "\n")
    
# print the initial and goal states
print("Inital State: ")
printState()
print("Goal State: ")
m1, c1, m2, c2 = 0, 0, 3, 30
printState()
m1, c1, m2, c2 = 3, 3, 0, 0

# start the solution in loop
while (m1 >= c1 or m1 == 0) and (m2 >= c2 or m2 == 0):
    rule = int(input("Enter rule: "))
    if rule == 1:  # take 1M,0C from Bank1 to Bank2
        m1 -= 1
        m2 += 1
    elif rule == 2:  # take 2M,0C from Bank1 to Bank2
        m1 -= 2
        m2 += 2
    elif rule == 3:  # take 1M,1C from Bank1 to Bank2
        m1 -= 1
        c1 -= 1
        m2 += 1
        c2 += 1
    elif rule == 4:  # take 0M,1C from Bank1 to Bank2
        c1 -= 1
        c2 += 1
    elif rule == 5:  # take 0M,2C from Bank1 to Bank2
        c1 -= 2
        c2 += 2
    elif rule == 6:  # take 1M,0C from Bank2 to Bank1
        m2 -= 1
        m1 += 1
    elif rule == 7:  # take 2M,0C from Bank2 to Bank1
        m2 -= 2
        m1 += 2
    elif rule == 8:  # take 1M,1C from Bank2 to Bank1
        m2 -= 1
        c2 -= 1
        m1 += 1
        c1 += 1
    elif rule == 9:  # take 0M,1C from Bank2 to Bank1
        c2 -= 1
        c1 += 1
    elif rule == 10:  # take 0M,2C from Bank2 to Bank1
        c2 -= 2
        c1 += 2

    printState()
    # break on successful transfer
    if m2 == 3 and c2 == 3:
        break;

if m2 != 3 and c2 != 3:
    print("Wrong rule selected. Missionary DEAD!!!")
else:
    print("MISSION SUCCESSFULL!!!")