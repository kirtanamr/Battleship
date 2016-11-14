Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
from random import randint
>>> board = []
>>> for x in range(5):
	board.append(["0"] * 5)
	def print_board(board):
		for row in board:
			print " ".join(row)
	print "Let's play battleship!"
	print_board(board)

	
Let's play battleship!
0 0 0 0 0
Let's play battleship!
0 0 0 0 0
0 0 0 0 0
Let's play battleship!
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Let's play battleship!
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Let's play battleship!
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
>>> def random_row(board):
	return randint(0, len(board) - 1)

>>> def random_col(board):
	return randint(0, len(board[0]) - 1)

>>> ship_row = random_row(board)
>>> ship_col = random_col(board)
>>> print ship_row
2
>>> print ship_col
1
>>> for turn in range(4):
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))
	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations! You sunk my battleship!"
		break
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			print "Oops! That's not even in the ocean."
		elif (board[guess_row][guess_col] == "X"):
			print "You guessed that one already."
		else:
			print "You missed my battlship!"
			if turn >= 3:
				print "Game over"
	print "Turn", turn + 1
	print_board(board)

	
Guess Row:3
Guess Col:1
You missed my battlship!
Turn 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Guess Row:1
Guess Col:2
You missed my battlship!
Turn 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Guess Row:3
Guess Col:2
You missed my battlship!
Turn 3
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Guess Row:2
Guess Col:2
You missed my battlship!
Game over
Turn 4
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
>>> 
