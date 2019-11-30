import pyglet

class presetButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 70
		self.label = pyglet.text.Label(text, x = xCoord, y = 70, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def onclick(self,x,y):
		if (self.x - 15 <= x <= self.x + 15) and(self.y - 22 <= y<= self.y +22):
			return True
			#is clicked
		else:
			return False
	def hover(self,x,y):
		if (self.x - 15 <= x <= self.x + 15) and(self.y - 22 <= y<= self.y +22):
			return True
		else:
			return False
			
class presetWindow(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(800, 640)
		self.label = pyglet.text.Label('The following are the instructions',font_size = 32, x = 400, y = 320, anchor_x = 'center', anchor_y = 'center')
	def on_draw(self):
		self.label.draw()

if __name__ == '__main__':
	window = instructionWindow(width = 800, height = 640, caption = 'Instructions', resizable = False)
	pyglet.app.run()