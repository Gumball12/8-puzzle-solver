# tools

# get user input
def getUserInput():
  return input("Select solver type [1: DFS, 2: BFS]: ")

# init
if __name__ == "__main__":
  # get user input
  inpt = getUserInput()

  while inpt != "1" and inpt != "2":
    print("Wrong type: " + inpt)
    inpt = getUserInput()

  print(inpt)
