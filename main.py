import japanize_kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition

# ウィンドウの背景色
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

Builder.load_file('menu.kv')
Builder.load_file('howto.kv')
Builder.load_file('gamekv.kv')

class MenuScreen(Screen):
    pass
 
class HowtoScreen(Screen):
    pass

class GameScreen(Screen):
	pass

class GameArea(GridLayout):

	def __init__(self, **kwargs):
		super(GameArea, self).__init__(**kwargs)

		# ゲームクラスのインスタンス生成
		import game
		self.game = game.Game(4)

		# ランダムに2のブロックを2個生成
		self.game.add_block_of_two()
		self.game.add_block_of_two()

		# ブロックの色と文字色
		self.colors = {
			0: {'background_color':(.7, .7, .7, 1), 'color':(0, 0, 0, 0), 'font_size':self.width / 2},
			2: {'background_color':(.83, .77, .68, 1), 'color':(0, 0, 0, 1), 'font_size':self.width / 2},
			4: {'background_color':(.96, .87, .7, 1), 'color':(0, 0, 0, 1), 'font_size':self.width / 2},
			8: {'background_color':(1, .62, .47, 1), 'color':(1, 1, 1, 1), 'font_size':self.width / 2},
			16: {'background_color':(.98, .5, .44, 1), 'color':(1, 1, 1, 1), 'font_size':self.width / 3},
			32: {'background_color':(1, .38, .27, 1), 'color':(1, 1, 1, 1), 'font_size':self.width / 3},
			64: {'background_color':(1, 0, 0, 1), 'color':(1, 1, 1, 1), 'font_size':self.width / 3},
			128: {'background_color':(1, 1, 0, .8), 'color':(0, 0, 0, 1), 'font_size':self.width / 4},
			256: {'background_color':(1, 1, 0, .85), 'color':(0, 0, 0, 1), 'font_size':self.width / 4},
			512: {'background_color':(1, 1, 0, .9), 'color':(0, 0, 0, 1), 'font_size':self.width / 4},
			1024: {'background_color':(1, 1, 0, .95), 'color':(0, 0, 0, 1), 'font_size':self.width / 5},
			2048: {'background_color':(1, 1, 0, 1), 'color':(0, 0, 0, 1), 'font_size':self.width / 5}
		}

		self.update_blocks()

	def update_blocks(self):
		# ブロックの削除
		self.clear_widgets()

		# ブロックの描画
		for y in range(self.game.get_blockcount()):
			for x in range(self.game.get_blockcount()):
				self.add_widget(Button(
					text = str(self.game.get_block(x, y)),
					font_size = self.colors[self.game.get_block(x, y)]['font_size'],
					background_normal = '',
					background_color = self.colors[self.game.get_block(x, y)]['background_color'],
					color = self.colors[self.game.get_block(x, y)]['color']
				))
    
	def on_touch_down(self, touch):
		if self.collide_point(*touch.pos):
			print(touch)
 
class GameApp(App):

	def __init__(self, **kwargs):
		super(GameApp, self).__init__(**kwargs)
		self.title = '2048'
 
	def build(self):
		Window.size = (360, 640)
		self.sm = ScreenManager()
		self.sm.add_widget(MenuScreen(name='menu'))
		self.sm.add_widget(HowtoScreen(name='howto'))
		self.sm.add_widget(GameScreen(name='game'))
		return self.sm

	def restart(self):
		self.sm.transition = NoTransition()
		self.sm.clear_widgets(screens=[self.sm.get_screen('game')])
		self.sm.add_widget(GameScreen(name='game'))
		self.sm.current = 'game'
		self.sm.transition = SlideTransition()
 
if __name__ == '__main__':
    GameApp().run()