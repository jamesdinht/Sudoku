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
				# print(cell.value, " ", value)
				if cell.value == str(value):
				# Mark rows
					for cell in row:
						cell.mark()
					#Create list of columns to be marked
					colIndeces.append(row.index(SudokuCell(str(value))))
		# Mark each column in the grid according to the list we generated
		for row in self.grid:
			for index in colIndeces:
				row[index].mark()

		return self

	# check if all cells are marked
	def isAllMArked(self):
		for row in self.grid:
			for cell in row:
				if not cell.marked:
					return False
		return True 

	# removes marks from all cells in the sudoku grid
	def unmarkAll(self):
		for row in self.grid:
			for cell in row:
				cell.unmark()

	# Function makes possible changes
	def solve(self):
		queue = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
		while len(queue) > 0:
			self = self.crosshatch(queue[0])
			# look at nonet
			# if there is ONE AND ONLY ONE zero, change that zero to queue[0]
			# else, move to next nonet
			for rowIndex in range(0, 6 + 1, 3):
				for colIndex in range(0, 6 + 1, 3):
					numBlankSpaces = 0
					makeChanges = duplicateInNonet = False
					for i in range(0, 2 + 1):
						for j in range(0, 2 + 1):
							# if you find a blank space, save its row and column and increase num of blank spaces
							if (not self.grid[rowIndex + i][colIndex + j].marked) and self.grid[rowIndex + i][colIndex + j].value == "0":
								print("Blank space found")
								blankRow = rowIndex + i
								blankCol = colIndex + j
								numBlankSpaces += 1

							# IF THE VALUE IS FOUND IN THE NONET YOU NEED TO BUST OUT OF THERE IMMEDIATELY
							if self.grid[rowIndex + i][colIndex + j].value == queue[0]:
								duplicateInNonet = True

							# if there are more than 1 unmarked blank spaces, can't make change
							if numBlankSpaces != 1:
								makeChanges = False
							# otherwise, you can make a change
							else:
								makeChanges = True		
					# print()

					if makeChanges and not duplicateInNonet:
						# print("Making change to grid")
						self.grid[blankRow][blankCol].value = queue[0]
						self = self.crosshatch(queue[0])
					# else:
					# 	print("Not making changes")


			# if every element is marked, remove that value from the Queue
			if self.isAllMArked():
				print("Popping Queue", queue[0])
				queue.pop(0)
			# else, move that value to the back of the queue
			else:
				print("Moving ", queue[0], " to back of Queue")
				queue.append(queue.pop(0))

			self.unmarkAll()



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