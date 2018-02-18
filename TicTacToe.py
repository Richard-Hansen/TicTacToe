def makeBoard():
	return [[" "," "," "],[" "," "," "],[" "," "," "]]
#Makes the 2D list that is used as a board

def printBoard(board):
	print "   0    1    2"
	print "0" + str(board[0])
	print "1" + str(board[1])
	print "2" + str(board[2])
#Prints the board

def checkTile(row, column, board):
	if ((row < 0 or row > 2) or (column < 0 or column > 2) or board[row][column] != " "):
		return False
	return True

def placeTile(row, column, tile, board):
	board[row][column] = tile

def checkWin(row, column, tile, board):
	if board[row][0] == board[row][1] == board[row][2] == tile:
		return True
	elif board[0][column] == board[1][column] == board[2][column] == tile:
		return True
	elif (board[0][0] == board[1][1] == board[2][2] == tile) or (board[0][2] == board[1][1] == board[2][0] == tile):
		return True
	else:
		return False

def playGame():
	b = makeBoard()
	characters = "XOXOXOXOX"

	for tile in characters:
		badInput = True

		row = 0
		column = 0

		while(badInput):
			row = input("Enter the row: ")
			column = input("Enter the column: ")

			if (checkTile(row, column, b) == False):
				print "You can't place a tile there!"
			else:
				badInput = False

		placeTile(row, column, tile, b)
		printBoard(b)

		if checkWin(row, column, tile, b) == True:
			print "Congratulations! Player %s has won!" % tile
			break
	print "Draw! Better luck next time!"


if __name__ == '__main__':
	playGame()
