"""
# 8-puzzle solver using DFS or BFS
# @author shj <https://github.com/Gumball12/8-puzzle-solver>
"""

from random import randint
from copy import deepcopy
from collections import deque

""" tools """

# get user input
def getUserInput():
  return input("Select solver type [1: DFS, 2: BFS]: ")

# generate an array
def getArray(len):
  a = list(range(len))
  return a

# chunk array by n
def chunkByN(a, n):
  return (a[i:i + n] for i in range(0, len(a), n)) # using generator

# swap arr values by index
def swap(arr, ia, ib):
  temporary = arr[ia]
  arr[ia] = arr[ib]
  arr[ib] = temporary

  return arr

# array to matrix
def arrayToMatrix(arr, size):
  return list(chunkByN(arr, size))

# unit testing
def testing():
  print('==========\nStart unit-test...\n==========')

  # init
  puzzle = Puzzle()
  tempPuzzle = deepcopy(puzzle) # copy previous puzzle instance
  directionNames = ['left', 'top', 'right', 'bottom']

  # check directions
  for d in range(0, 4):
    # check movable
    if (puzzle.isMovable()[d]):
      # move to direction
      puzzle = puzzle.move(d) # update puzzle

      # check updated
      if (str(puzzle) == str(tempPuzzle)): # error
        print('failed to', directionNames[d], 'direction test: puzzle instance did not updated')
        return False # failure
      else: # success
        print('success', directionNames[d], 'direction test')
        tempPuzzle = deepcopy(puzzle) # update tempPuzzle
    else:
      print('can not move to the', directionNames[d], 'direction')

  return True # success

# append to array with multiple arguments
def append(arr, *items):
  for i in items:
    arr.append(i)

  return arr

""" process """

# Puzzle class
class Puzzle:
  # constructor
  def __init__(self, matrix = None, size = 3): # default size is 3
    # init matrix
    if (matrix):
      self.matrix = matrix
      self.size = len(matrix)
    else:
      self.matrix = arrayToMatrix(getArray(size * size), size)
      self.size = size
      self.shuffle()

  # move operator
  # @param {number} op operators (0: left, 1: top, 2: right, 3: bottom)
  def move(self, op):
    # operator guard
    if (not(0 <= int(op) and int(op) <= 4)):
      return False

    # check movable
    if (not(self.isMovable()[op])):
      return False

    arr = sum(self.matrix, []) # matrix to array
    ind = arr.index(0) # target index
    swapInd = ind # swap index

    if (op == 0): # left
      swapInd = ind - 1
    elif (op == 1): # top
      swapInd = ind - self.size
    elif (op == 2): # right
      swapInd = ind + 1
    elif (op == 3): # bottom
      swapInd = ind + self.size
    else: # wroing direction
      return False

    # unmutable method
    # self.matrix = arrayToMatrix(swap(arr, ind, swapInd), self.size)

    # return new Puzzle
    return Puzzle(arrayToMatrix(swap(arr, ind, swapInd), self.size))

  # check target is movable
  def isMovable(self):
    arr = sum(self.matrix, []) # matrix to array
    ind = arr.index(0) # find target index

    size = self.size

    # generate status
    left = ind % size != 0
    top = ind >= size
    right = (ind + 1) % size != 0
    bottom = len(arr) - size > ind

    # return status
    return (left, top, right, bottom)

  # shuffle this matrix
  def shuffle(self):
    for i in range(randint(50, 100)):
      direction = randint(0, 3)
      if (self.isMovable()[direction]):
        self.matrix = self.move(direction).matrix

  # toString
  def __str__(self):
    return ', '.join(map(str, self.matrix)) # map: string guard

# process
def process():
  # create puzzle instances
  size = 4

  puzzle = Puzzle(None, size)
  # puzzle = Puzzle([[1, 7, 4], [8, 0, 2], [3, 6, 5]])
  # puzzle = Puzzle([[1, 2, 5], [3, 4, 8], [0, 6, 7]])
  goal = Puzzle(arrayToMatrix(getArray(size * size), size)) # goal state

  print('Create Puzzle instance', puzzle)
  print('Create goal state', goal)

  # get user input
  inpt = getUserInput()

  while inpt != "1" and inpt != "2":
    print("Wrong type: " + inpt)
    inpt = getUserInput()

  # define arrays using deque
  opens = deque([puzzle])
  closes = deque([])

  # searching
  while len(opens) != 0:
    # get leftmost element
    x = opens.popleft()

    if (str(x) == str(goal)): # when success
      print('length of closed:', len(closes))
      return True
    else: # before success
      # put x into the closes array
      closes.append(str(x))

      # append(opens, *[x.move(d) for d in range(0, 4) if x.isMovable()[d] and str(x.move(d)) not in closes])

      movable = x.isMovable()

      # generate x's children
      for d in range(0, 4):
        if (movable[d]):
          moved = x.move(d)

          if (str(moved) not in closes):
            if (inpt == 1): # DFS
              opens.appendleft(moved)
            else: # BFS
              opens.append(moved)

  return False

# init
if __name__ == "__main__":
  if (testing()):
    print('==========\nSuccess unit testing\n==========\n')
    result = process()
    print("solved" if result else "failed")
  else:
    print('==========\nFailed to unit testing\n==========\n')
