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
			for cell in row:
				print(str(cell), " ", end = "")
			print()
		print("\n")

	# Crosshatching algorithm to solve Sudoku Game
	def crosshatch(self, value):
		colIndeces = []
		cellValue = str(value)
		for row in self.grid:
			for cell in row:
				print(cell.value, " ", value)
				if cell.value == str(value):
					print('Value in row')
				# Mark rows
					for cell in row:
						print('Mark row')
						cell.mark()

					#Mark columns
					colIndeces.append(row.index(SudokuCell(str(value))))

		for row in self.grid:
			for index in colIndeces:
				print('Mark col')
				row[index].mark()

		return self



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

	def __eq__(self, other):
		return self.value == other.value

	def __str__(self):
		if self.marked:
			return self.value + 'm'
		else:
			return self.value + ' '