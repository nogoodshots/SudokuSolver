# Lets solve a Sudoku problem

class Sudoku:
	
	def __init__(self, mag=9, givens=[]):
	  self.magnitude = mag
	  self.cells = {}
	  for row in range(mag):
	  	self.cells[row] = {}
	  	for col in range(mag):
	  		self.cells[row][col] = Cell(row, col, [x + 1 for x in range(mag)])
	  for g in givens:
	  	row = g[0]
	  	col = g[1]
	  	value = g[2]
	  	self.solve(row, col, value)
	  	
	def solve(self, row, col, value):
		debug_cell = (3, 6)
		debugging = row == debug_cell[0] and col == debug_cell[1]
		print(f"Solving [{row},{col}] to {value}")
		self.cells[row][col].solve(value)
		discovered = []
		for c in self.in_local(row, col):
			if not c.solved:
				c.eliminate(value)
				if c.solved:
					discovered.append(c)
		for c in self.in_row(row, col, False):
			if not c.solved:
				c.eliminate(value)
				if c.solved:
					discovered.append(c)
		for c in self.in_col(row, col, False):
			if not c.solved:
				c.eliminate(value)
				if c.solved:
					discovered.append(c)
		for d in discovered:
			self.solve(d.row, d.col, d.possibilities[0])
	  			
	def in_row(self, row, col, include = True):
		for c in range(self.magnitude):
			if c != col or include:
				yield self.cells[row][c]
				
	def in_col(self, row, col, include = True):
		for c in range(self.magnitude):
			if c != row or include:
				yield self.cells[c][col]
				
	def in_local(self, row, col, include = True):
		x = col // 3
		y = row // 3
		for r in range(y * 3, (y * 3) + 3):
			for c in range(x * 3, (x * 3) + 3):
				if include or not (row == r and col == c):
				  yield self.cells[r][c]
				
	def unsolved(self):
		for row in range(self.magnitude):
			for col in range(self.magnitude):
				if not self.cells[row][col].solved:
				  yield self.cells[row][col]
				  
	def print(self):
		for y in range(self.magnitude):
			if y > 0 and y % 3 == 0:
				print("---------")
			output = ""
			for x in range(self.magnitude):
				if x > 0 and x % 3 == 0:
					output += "|"
				c = self.cells[y][x]
				if c.solved:
				  output += str(c.possibilities[0])
				else:
					output += " "
			print(output)
			
	def find_shared_fate(self, cell, candidates):
		progress = False
		# look for n-1 other cell with the same n possibilities
		shared_fate = [sf for sf in candidates if cell.possibilities == sf.possibilities]
		if len(cell.possibilities) == len(shared_fate):
			for x in candidates:
				if not x in shared_fate:
					progress = True
					for v in cell.possibilities:
						x.eliminate(v)
		return progress
		
	def think(self):
		# Get an unsolved cell and try and check each remaining possibility
		for cell in self.unsolved():
			for value in cell.possibilities:
				candidates_in_row = [x for x in self.in_row(cell.row, cell.col) if value in x.possibilities]
				if len(candidates_in_row) == 1:
					print(f"Solving in row")
					self.solve(candidates_in_row[0].row, candidates_in_row[0].col, value)
					return True
				if len(candidates_in_row) == 0:
					raise ProgramFail
				if self.find_shared_fate(cell, candidates_in_row):
					return True
				candidates_in_col = [x for x in self.in_col(cell.row, cell.col) if value in x.possibilities]
				if len(candidates_in_col) == 1:
					print(f"Solving in col")
					self.solve(candidates_in_col[0].row, candidates_in_col[0].col, value)
					return True
				if len(candidates_in_col) == 0:
					raise ProgramFail
				if self.find_shared_fate(cell, candidates_in_col):
					return True
				candidates_in_local = [x for x in self.in_local(cell.row, cell.col) if value in x.possibilities]
				if len(candidates_in_local) == 1:
					print(f"Solving in local")
					self.solve(candidates_in_local[0].row, candidates_in_local[0].col, value)
					return True
				if len(candidates_in_local) == 0:
					raise ProgramFail
				if self.find_shared_fate(cell, candidates_in_local):
					return True
		return False
				
			
		
	  	
class Cell:
	
	solved = False
	
	def __init__(self, row, col, possibilities):
		self.row = row
		self.col = col
		self.possibilities = possibilities
		if len(self.possibilities) == 1:
			self.solved = True
		if len(self.possibilities) == 0:
			raise IllegalArgument
	
	def solve(self, result):
		self.solved = True
		self.possibilities = [r for r in self.possibilities if r == result]
		if len(self.possibilities) != 1:
			raise ProgramFail
			
	def eliminate(self, value):
		self.possibilities = [r for r in self.possibilities if r != value]
		if len(self.possibilities) == 0:
			raise ProgramFail
		if len(self.possibilities) == 1:
			print(f"self solving {self.possibilities[0]} at {self.row},{self.col}")
			self.solved = True
	


