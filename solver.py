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

boardDifficult = np.array([[0,0,0,6,0,0,4,0,0],
	[7,0,0,0,0,3,6,0,0],
	[0,0,0,0,9,1,0,8,0],
	[0,0,0,0,0,0,0,0,0],
	[0,5,0,1,8,0,0,0,3],
	[0,0,0,3,0,6,0,4,5],
	[0,4,0,2,0,0,0,6,0],
	[9,0,3,0,0,0,0,0,0],
	[0,2,0,0,0,0,1,0,0]])

boardHard = np.array([[0,2,0,0,0,0,0,0,0],
	[0,0,0,6,0,0,0,0,3],
	[0,7,4,0,8,0,0,0,0],
	[0,0,0,0,0,3,0,0,2],
	[0,8,0,0,4,0,0,1,0],
	[6,0,0,5,0,0,0,0,0],
	[0,0,0,0,1,0,7,8,0],
	[5,0,0,0,0,9,0,0,0],
	[0,0,0,0,0,0,0,4,0]])

boardWrong = np.array([[0,2,0,0,0,0,0,0,0],
	[0,0,0,6,0,0,0,0,3],
	[0,7,4,0,8,0,0,0,0],
	[0,0,0,0,0,3,0,0,2],
	[0,8,0,0,4,0,0,1,0],
	[6,0,0,5,0,0,0,0,0],
	[0,0,0,0,1,0,7,8,0],
	[5,0,0,0,0,9,4,0,0],
	[0,0,0,0,0,0,0,4,0]])


def easySolve(board):
	notSolved = True

	while notSolved:
		notSolved = False

		for i in np.arange(9):
			for j in np.arange(9):

				if board[i][j] == 0:
					possibleHorizontals = checkHorizontal(board, i)
					possibleVerticals = checkVertical(board, j)
					possibleSquare = checkSquare(board,i,j)

					possibles = list( set(possibleVerticals) & set(possibleHorizontals) & set(possibleSquare))

					if len(possibles) == 1:
						board[i][j] = possibles[0]
					notSolved = True
	print(board)


def checkHorizontal(board, x):
	row = set(board[x])
	row.remove(0)
	possibles = []
	for a in np.arange(1, 10):
		if a not in row:
			possibles.append(a)
	return possibles

def checkVertical(board, y):
	column = set(board[:, y])
	column.remove(0)
	possibles = []
	for b in np.arange(1, 10):
		if b not in column:
			possibles.append(b)
	return possibles

def checkSquare(board, x, y):
	squareX = (x // 3) * 3
	squareY = (y // 3) * 3
	subArray = board[squareX:squareX+3,squareY:squareY+3]
	square = set(subArray.flatten())
	possibles = []
	for c in np.arange(1, 10):
		if c not in square:
			possibles.append(c)
	return possibles

def checkIntegrity(board):
	for i in np.arange(9):
		row = board[i].tolist()
		row = [i for i in row if i != 0]

		column = board[:, i].tolist()
		column = [i for i in column if i != 0]

		if (len(set(column)) != len(column)):
			return False

		if (len(set(row)) != len(row)):
			return False

		for j in np.arange(9):
			squareX = (i // 3) * 3
			squareY = (j // 3) * 3
			subArray = board[squareX:squareX+3,squareY:squareY+3]
			square = subArray.flatten().tolist()
			square = [i for i in square if i != 0]
			if len(set(square)) != len(square):
				return False
	
	return True

def find_zero(board):
	for i in np.arange(9):
		for j in np.arange(9):
			if board[i][j] == 0:
				return i,j
	return None

def backTrackSolve(board):

	zeros = find_zero(board)
	if not zeros:
		print(board)
		return True
		
	else:
		i,j = zeros

	for num in np.arange(1,10):
		board[i][j] = num
		
		if checkIntegrity(board):

			if backTrackSolve(board):
				return True

		board[i][j] = 0

	return False

backTrackSolve(boardHard)

