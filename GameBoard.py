# Represents a single Sudoku Game Board
class GameBoard:
	def __init__(self, gridlist):
		self.grid = []
		cellRow = []
		for num in gridlist:
			cellRow.append(SudokuCell(num))
			if len(cellRow) == 9:
				self.grid.append(list(cellRow))
				cellRow.clear()


			# self.grid.append(SudokuCell(num, grid.index))
			


	def printGrid(self):
		for row in self.grid:
			for cells in row:
				print(cells.value, " ", end = "")
			print()
		print("\n")

	# Crosshatching algorithm to solve Sudoku Game
	# def crosshatch(self, value):
	# 	for num in self.grid:
	# 		if num == value:
	# 			# mark row and column
	# 	return



	# def solve():
	# 	queue 1-9
	# 	while not solved
	# 		crosshatch(queue)
	# 		check if 


# Represents a single cell on the Sudoku Game Board
class SudokuCell:
	def __init__(self,value):
		self.value = value
		self.marked = False

	def mark(self):
		self.marked = True

	def unmark(self):
		self.marked = False