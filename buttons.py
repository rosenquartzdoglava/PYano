import pyglet

class Button():
	def __init__(self, xCoord, yCoord, text, batcheu):
		self.x = xCoord
		self.y = yCoord
		self.label = pyglet.text.Label(text, x = xCoord, font_size = 36, y = yCoord, anchor_x = 'center', anchor_y = 'center', batch = batcheu)
	def onclick(self, x, y):
		if (self.x - 30 <= x <= self.x + 30) and (self.y - 30 <= y <= self.y + 30):
			return True
		else:
			return False

class toneButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 675
		self.label = pyglet.text.Label(text, x = xCoord, y = 675, font_size = 32, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def reset():
		pass
	def onclick(self,x,y):
		if (self.x - 50 <= x <= self.x + 50) and(self.y - 25 <= y<= self.y +25):
			return True
			#is clicked
		else:
			return False
	def hover(self,x,y):
		if (self.x - 50 <= x <= self.x + 50) and(self.y - 25 <= y<= self.y +25):
			return True
		else:
			return False

def resetTone(tonelist, i):
	for x in range(len(tonelist)):
		if x != i:
			tonelist[x].label.font_size = 32

class keyButton():
	def __init__(self, xCoord, text, buttons, type):
		self.x = xCoord
		self.y = 615
		self.type = type # how large is 
		self.label = pyglet.text.Label(text, x = xCoord, y = 615, font_size = 28, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def reset():
		pass
	def onclick(self,x,y):
		if self.type == 0:
			if (self.x - 15 <= x <= self.x + 15) and(self.y - 15 <= y<= self.y +15):
				return True
		else:
			if (self.x - 25 <= x <= self.x + 25) and(self.y - 15 <= y<= self.y +15):
				return True
	def hover(self,x,y):
		if self.type == 0:
			if (self.x - 15 <= x <= self.x + 15) and(self.y - 15 <= y<= self.y +15):
				return True
			else:
				return False
		else:
			if (self.x - 25 <= x <= self.x + 25) and(self.y - 15 <= y<= self.y +15):
				return True
			else:
				return False

def resetKey(keylist, i):
	for x in range(len(keylist)):
		if x != i:
			keylist[x].label.font_size = 28