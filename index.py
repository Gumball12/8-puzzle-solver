"""
# 8-puzzle solver using DFS or BFS
# @author shj <https://github.com/Gumball12/8-puzzle-solver>
"""

from random import shuffle
from copy import deepcopy

""" tools """

# get user input
def getUserInput():
  return input("Select solver type [1: DFS, 2: BFS]: ")

# generate an array
def getArray(len):
  a = list(range(len))
  return a

# shuffle array
def shuffleArray(a):
  shuffle(a)
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
      puzzle.move(d)

      # check updated
      if (str(puzzle) == str(tempPuzzle)): # error
        print('failed to', directionNames[d], 'direction test: puzzle instance did not updated')
        return False # failure
      else:
        print('success', directionNames[d], 'direction test')
        tempPuzzle = deepcopy(puzzle) # update tempPuzzle
    else:
      print('can not move to the', directionNames[d], 'direction')

  return True # success

""" process """

# Puzzle class
class Puzzle:
  # constructor
  def __init__(self, size = 3): # default size is 3
    # init matrix
    self.matrix = arrayToMatrix(shuffleArray(getArray(size * size)), size)
    self.size = size

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

    self.matrix = arrayToMatrix(swap(arr, ind, swapInd), self.size)

    # return new matrix
    return self.matrix

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

  # toString
  def __str__(self):
    return ', '.join(map(str, self.matrix)) # map: string guard

# process
def process():
  # get user input
  inpt = getUserInput()

  while inpt != "1" and inpt != "2":
    print("Wrong type: " + inpt)
    inpt = getUserInput()

  # create puzzle instance
  puzzle = Puzzle()

# init
if __name__ == "__main__":
  if (testing()):
    print('==========\nSuccess unit testing\n==========\n')
    process()
  else:
    print('==========\nFailed to unit testing\n==========\n')
