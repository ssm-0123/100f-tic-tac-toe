#!python3

def displayString(board):
  """
  function should create a string that can be displayed using a print command
  this function should have no actual print commands in it
  
  input:
  list board: the game board data:
  7 8 9
  4 5 6
  1 2 3
  
  eg 
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  should display:
  - - X
  X O -
  O - -
  
  return value
  str the gameboard
  """
  result =""
  for i in range(6,9):
    if board[i] == 0:
      result = result + "-"
    else:
      result = result + f"{board[i]}"
    if i != 8:
      result = result +" "
  result = result +"\n"

  for i in range(3,6):
    if board[i] == 0:
      result = result + "-"
    else:
      result = result + f"{board[i]}"
    if i != 5:
      result = result +" "
  result = result +"\n"

  for i in range(0,3):
    if board[i] == 0:
      result = result + "-"
    else:
      result = result + f"{board[i]}"
    if i != 2:
      result = result +" "

  return result

def main():
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  assert displayString(board) == "- - X\nX O -\nO - -"
  board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
  assert displayString(board) == "X - X\nO O -\n- O X"

if __name__ == "__main__":
  main()
