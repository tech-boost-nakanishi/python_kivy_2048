import random

class Game():

	def __init__(self, blockcount):
		self.blockcount = blockcount
		self.blocks = [[0] * self.blockcount for i in range(self.blockcount)]

	def get_blockcount(self):
		return self.blockcount
	
	def get_blocks(self):
		return self.blocks

	def get_block(self, x, y):
		return self.blocks[x][y]

	def set_block(self, x, y, value):
		self.blocks[x][y] = value

	def has_zero_value(self):
		for y in range(self.get_blockcount()):
			for x in range(self.get_blockcount()):
				if self.get_block(x, y) == 0:
					return True

		return False

	def add_block_of_two(self):
		while True:
			x = random.randint(0, self.get_blockcount() - 1)
			y = random.randint(0, self.get_blockcount() - 1)

			if self.get_block(x, y) == 0:
				self.set_block(x, y, 2)
				break