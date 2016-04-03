# Represents a single cell on the Sudoku Game Board
class SudokuCell:
	def __init__(self,value):
		self.value = value
		self.marked = False

	def mark(self):
		self.marked = True

	def unmark(self):
		self.marked = False