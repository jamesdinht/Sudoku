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

	# check if all cells are marked
	def isAllMarked(self):
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

	# Crosshatching algorithm to solve Sudoku Game
	def crosshatch(self, value, mark=True):
		colIndeces = []
		cellValue = str(value)
		for row in self.grid:
			for cell in row:
				# print(cell.value, " ", value)
				if cell.value == cellValue:
						# Mark rows
						for cell in row:
							if mark:
								cell.mark()
							else:
								if cellValue in cell.pencilInList:
									cell.pencilInList.remove(cellValue)
						#Create list of columns to be marked
						colIndeces.append(row.index(SudokuCell(str(value))))
		# Mark each column in the grid according to the list we generated
		for row in self.grid:
			for index in colIndeces:
				if mark:
					row[index].mark()
				else:
					if cellValue in row[index].pencilInList:
						row[index].pencilInList.remove(cellValue)

		return self

	def fillIn(self, row, col, replacementValue):
		self.grid[row][col].value = replacementValue

	def pencilIn(self, pencilInList, nonetRow, nonetCol):
		for i in range(0, 2 + 1):
			for j in range(0, 2 + 1):
				if self.grid[nonetRow + i][nonetCol + j].isBlank():
					self.grid[nonetRow + i][nonetCol + j].initPencilInList(pencilInList)
					for num in range(1, 10):
						self.crosshatch(num, mark=False)
					if len(pencilInList) == 1:
						self.fillIn(nonetRow + i, nonetCol + j, pencilInList[0])
						pencilInList.remove(pencilInList[0])
						self.pencilIn(pencilInList, nonetRow, nonetCol)

		return self

	# Function makes possible changes
	def solve(self):
		queue = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
		numOfPasses = 0

		while queue and numOfPasses <= len(queue)*3:
			self = self.crosshatch(queue[0])
			# look at nonet
			# if there is ONE AND ONLY ONE zero, change that zero to queue[0]
			# else, move to next nonet
			for rowIndex in range(0, 6 + 1, 3):
				for colIndex in range(0, 6 + 1, 3):
					numBlankSpaces = 0
					makeChanges = duplicateInNonet = False
					pencilInList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

					for i in range(0, 2 + 1):
						for j in range(0, 2 + 1):

							if numOfPasses <= 18:
								# if you find a blank space, save its row and column and increase num of blank spaces
								if (not self.grid[rowIndex + i][colIndex + j].marked) and self.grid[rowIndex + i][colIndex + j].value == "0":
									blankRow = rowIndex + i
									blankCol = colIndex + j
									numBlankSpaces += 1

								# Prepare penciling in list for all blank spaces in a single nonet
								if self.grid[rowIndex + i][colIndex + j].value in pencilInList:
									pencilInList.remove(self.grid[rowIndex + i][colIndex + j].value)

								# IF THE VALUE IS FOUND IN THE NONET YOU NEED TO BUST OUT OF THERE IMMEDIATELY
								if self.grid[rowIndex + i][colIndex + j].value == queue[0]:
									duplicateInNonet = True

								# if there are more than 1 unmarked blank spaces, can't make change
								if numBlankSpaces != 1:
									makeChanges = False
								# otherwise, you can make a change
								else:
									makeChanges = True		

					if numOfPasses <= 18:
						if makeChanges and not duplicateInNonet:
							self.fillIn(blankRow, blankCol, queue[0])
							self = self.crosshatch(queue[0])

					if numOfPasses >= 18:
						self.pencilIn(pencilInList, rowIndex, colIndex)

			# if every element is marked, remove that value from the Queue
			if self.isAllMarked():
				queue.pop(0)
			# else, move that value to the back of the queue
			else:
				queue.append(queue.pop(0))
			numOfPasses += 1
			self.unmarkAll()



# Represents a single cell on the Sudoku Game Board
class SudokuCell:
	def __init__(self,value):
		self.value = value
		self.pencilInList = []
		self.marked = False

	def initPencilInList(self, pencilInList):
		self.pencilInList = pencilInList

	def mark(self):
		self.marked = True

	def unmark(self):
		self.marked = False

	def isBlank(self):
		return self.value == '0'

	def __eq__(self, other):
		return self.value == other.value

	def __str__(self):
		if self.marked:
			return self.value + 'm'
		else:
			return self.value + ' '