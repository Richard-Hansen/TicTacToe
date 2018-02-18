def makeBoard():
	return [[" "," "," "],[" "," "," "],[" "," "," "]]
#Makes the 2D list that is used as a board

def printBoard(board):
	print board[0]
	print board[1]
	print board[2]

def placeTile(row, column, tile, board):
	if (board[row][column] != " "):
		return False

	board[row][column] = tile
	return True

if __name__ == '__main__':
	b = makeBoard()
	printBoard(b)
	placeTile(1,1,"X",b)
	printBoard(b)
