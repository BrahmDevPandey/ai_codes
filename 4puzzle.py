# program to play 4-puzzle problem
matrix = [3, 1, 0, 2]   # initial state
position = 2  # position of blank in matrix
final_state = [1, 2, 3, 0]  # goal state

def printMatrix():
  print(matrix[0], matrix[1])
  print(matrix[2], matrix[3])

printMatrix()
while not matrix == final_state:
  move = str(input("Enter move (U/D/L/R): "))

  if move == "U":
    if position not in [0, 1]:
      new_position = position - 2
  elif move == "D":
    if position not in [2, 3]:
      new_position = position + 2
  elif move == "R":
    if position not in [1, 3]:
      new_position = position + 1
  elif move == "L":
    if position not in [0, 2]:
      new_position = position - 1
  else:
    print("Invalid move")

  if not position == new_position:   # swap the elements at position and new position
    temp = matrix[new_position]
    matrix[new_position] = matrix[position]
    matrix[position] = temp
    position = new_position

  printMatrix()   # print the new matrix
