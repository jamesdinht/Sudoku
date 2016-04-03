#Python

def getSudokuGrid(fileName):
	sudokuFile = open(fileName, 'r')
	
	for line in sudokuFile:
		print(line)

def main(fileName):
	getSudokuGrid(fileName)

if __name__ == '__main__':
	main('sudoku.txt')