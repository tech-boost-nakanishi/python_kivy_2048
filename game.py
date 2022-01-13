class Game():

	def __init__(self, blockcount):
		self.blockcount = blockcount
		self.blocks = [[0] * 4 for i in range(4)]

	def get_blockcount(self):
		return self.blockcount
	
	def get_blocks(self):
		return self.blocks

	def get_block(self, x, y):
		return self.blocks[x][y]

	def set_block(self, x, y, value):
		self.blocks[x][y] = value