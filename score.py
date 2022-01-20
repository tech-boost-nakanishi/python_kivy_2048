import sqlite3

class Score():

	def __init__(self):
		self.score = 0
		self.dbname = 'res/database/score.db'

		# ベストスコアの設定
		conn = sqlite3.connect(self.dbname)
		cur = conn.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS scores(id integer, bestscore integer)')
		cur.execute('INSERT INTO scores(id,bestscore) SELECT 1,0 WHERE NOT EXISTS(SELECT 1 FROM scores WHERE id = 1)')
		conn.commit()
		cur.close()
		conn.close()

	def get_score(self):
		return self.score

	def set_score(self, value):
		self.score = value

	def get_bestscore(self):
		conn = sqlite3.connect(self.dbname)
		cur = conn.cursor()
		bestscore = cur.execute('SELECT bestscore FROM scores WHERE id = 1').fetchone()[0]
		cur.close()
		conn.close()
		return bestscore

	def set_bestscore(self, value):
		conn = sqlite3.connect(self.dbname)
		cur = conn.cursor()
		cur.execute('UPDATE scores SET bestscore = "{}" WHERE id = 1'.format(value))
		conn.commit()
		cur.close()
		conn.close()