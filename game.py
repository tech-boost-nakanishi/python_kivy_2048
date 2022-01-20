import random

class Game():

	def __init__(self, blockcount):
		self.blockcount = blockcount
		self.moved = False
		self.blocks = [[0] * self.blockcount for i in range(self.blockcount)]

		# スコアクラスのインスタンス生成
		import score
		self.score = score.Score()

		self.infos = {
			'up': {'startX': 0, 'startY': 0, 'moveX': 0, 'moveY': 1},
			'left': {'startX': 0, 'startY': 0, 'moveX': 1, 'moveY': 0},
			'down': {'startX': self.blockcount - 1, 'startY': self.blockcount - 1, 'moveX': 0, 'moveY': -1},
			'right': {'startX': self.blockcount - 1, 'startY': self.blockcount - 1, 'moveX': -1, 'moveY': 0}
		}

	def get_moved(self):
		return self.moved

	def set_moved(self, state):
		self.moved = state

	def get_blockcount(self):
		return self.blockcount
	
	def get_blocks(self):
		return self.blocks

	def get_block(self, x, y):
		return self.blocks[x][y]

	def set_block(self, x, y, value):
		self.blocks[x][y] = value

	def get_num_count(self, num):
		count = 0
		for y in range(self.get_blockcount()):
			for x in range(self.get_blockcount()):
				if self.get_block(x, y) == num:
					count += 1

		return count

	def add_block_of_two(self):
		while True:
			x = random.randint(0, self.get_blockcount() - 1)
			y = random.randint(0, self.get_blockcount() - 1)

			if self.get_block(x, y) == 0:
				self.set_block(x, y, 2)
				break

	def can_move(self):
		for y in range(self.get_blockcount()):
			for x in range(self.get_blockcount()):
				if self.get_block(x, y) == 0:
					return True

				for i in range(4):
					if i == 0:
						if y - 1 >= 0:
							if self.get_block(x, y - 1) == self.get_block(x, y):
								return True
					elif i == 1:
						if y + 1 <= self.get_blockcount() - 1:
							if self.get_block(x, y + 1) == self.get_block(x, y):
								return True
					elif i == 2:
						if x - 1 >= 0:
							if self.get_block(x - 1, y) == self.get_block(x, y):
								return True
					elif i == 3:
						if x + 1 <= self.get_blockcount() - 1:
							if self.get_block(x + 1, y) == self.get_block(x, y):
								return True

		return False

	def move_blocks(self, direct):
		self.set_moved(False)
		for i in range(self.get_blockcount()):
			cx = self.infos[direct]['startX'] + (i * self.infos[direct]['moveY'])
			cy = self.infos[direct]['startY'] + (i * self.infos[direct]['moveX'])

			# ブロックをdirect方向に寄せる
			for j in range(self.get_blockcount()):
				dx, dy = cx, cy
				if self.infos[direct]['moveX'] != 0:
					dx += (self.infos[direct]['moveX']) * (self.get_blockcount() - 1)
				if self.infos[direct]['moveY'] != 0:
					dy += (self.infos[direct]['moveY']) * (self.get_blockcount() - 1)
				px = dx - self.infos[direct]['moveX']
				py = dy - self.infos[direct]['moveY']
				while True:
					if px < 0 or py < 0 or px >= self.get_blockcount() or py >= self.get_blockcount():
						break

					if self.get_block(px, py) == 0:
						if self.get_block(dx, dy) > 0:
							self.set_moved(True)
						self.set_block(px, py, self.get_block(dx, dy))
						self.set_block(dx, dy, 0)

					px -= self.infos[direct]['moveX']
					py -= self.infos[direct]['moveY']
					dx -= self.infos[direct]['moveX']
					dy -= self.infos[direct]['moveY']

			# 隣のブロックと数字が一緒なら結合
			dx, dy = cx, cy
			nx = dx + self.infos[direct]['moveX']
			ny = dy + self.infos[direct]['moveY']
			while True:
				if nx < 0 or ny < 0 or nx >= self.get_blockcount() or ny >= self.get_blockcount():
					break

				if self.get_block(dx, dy) == self.get_block(nx, ny) and self.get_block(dx, dy) > 0:
					self.score.set_score(self.score.get_score() + (self.get_block(dx, dy) * 2))
					self.set_block(dx, dy, self.get_block(dx, dy) * 2)
					self.set_block(nx, ny, 0)
					self.set_moved(True)

				nx += self.infos[direct]['moveX']
				ny += self.infos[direct]['moveY']
				dx += self.infos[direct]['moveX']
				dy += self.infos[direct]['moveY']

			# ブロックをdirect方向に寄せる
			for j in range(self.get_blockcount()):
				dx, dy = cx, cy
				if self.infos[direct]['moveX'] != 0:
					dx += (self.infos[direct]['moveX']) * (self.get_blockcount() - 1)
				if self.infos[direct]['moveY'] != 0:
					dy += (self.infos[direct]['moveY']) * (self.get_blockcount() - 1)
				px = dx - self.infos[direct]['moveX']
				py = dy - self.infos[direct]['moveY']
				while True:
					if px < 0 or py < 0 or px >= self.get_blockcount() or py >= self.get_blockcount():
						break

					if self.get_block(px, py) == 0:
						self.set_block(px, py, self.get_block(dx, dy))
						self.set_block(dx, dy, 0)

					px -= self.infos[direct]['moveX']
					py -= self.infos[direct]['moveY']
					dx -= self.infos[direct]['moveX']
					dy -= self.infos[direct]['moveY']