import pyglet

class instructionWindow(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(800, 640)
		self.label = pyglet.text.Label('The following are the instructions',font_size = 32, x = 400, y = 320, anchor_x = 'center', anchor_y = 'center')
	def on_draw(self):
		self.label.draw()

if __name__ == '__main__':
	window = instructionWindow(width = 800, height = 640, caption = 'Instructions', resizable = False)
	pyglet.app.run()