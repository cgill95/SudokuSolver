import numpy as np


#gameBoard = np.zeros((9,9), dtype=int)

boardEasy = np.array([[0,0,0,2,6,0,7,0,1],
	[6,8,0,0,7,0,0,9,0],
	[1,9,0,0,0,4,5,0,0],
	[8,2,0,1,0,0,0,4,0],
	[0,0,4,6,0,2,9,0,0],
	[0,5,0,0,0,3,0,2,8],
	[0,0,9,3,0,0,0,7,4],
	[0,4,0,0,5,0,0,3,6],
	[7,0,3,0,1,8,0,0,0]])

boardHard = np.array([[0,2,0,0,0,0,0,0,0],
	[0,0,0,6,0,0,0,0,3],
	[0,7,4,0,8,0,0,0,0],
	[0,0,0,0,0,3,0,0,2],
	[0,8,0,0,4,0,0,1,0],
	[6,0,0,5,0,0,0,0,0],
	[0,0,0,0,1,0,7,8,0],
	[5,0,0,0,0,9,0,0,0],
	[0,0,0,0,0,0,0,4,0]])


def solve(board):
	notSolved = True

	while notSolved:
		notSolved = False

		for i in np.arange(9):
			for j in np.arange(9):
				#print(i,j)
				if board[i][j] == 0:
					possibleHorizontals = checkHorizontal(board, i)
					possibleVerticals = checkVertical(board, j)
					possibleSquare = checkSquare(board,i,j)
					#print(possibleVerticals)
					#print(possibleHorizontals)
					possibles = list( set(possibleVerticals) & set(possibleHorizontals) & set(possibleSquare))
					#print(possibles)
					if len(possibles) == 1:
						#print(possibles[0])
						board[i][j] = possibles[0]
					notSolved = True
	print(board)
	



def checkHorizontal(board, x):
	row = set(board[x])
	row.remove(0)
	possibles = []
	for i in np.arange(1, 10):
		if i not in row:
			possibles.append(i)
	return possibles

def checkVertical(board, y):
	column = set(board[:, y])
	column.remove(0)
	possibles = []
	for i in np.arange(1, 10):
		if i not in column:
			possibles.append(i)
	return possibles

def checkSquare(board, x, y):
	squareX = (x // 3) * 3
	squareY = (y // 3) * 3
	subArray = board[squareX:squareX+3,squareY:squareY+3]
	square = set(subArray.flatten())
	possibles = []
	for i in np.arange(1, 10):
		if i not in square:
			possibles.append(i)
	return possibles

solve(boardHard)