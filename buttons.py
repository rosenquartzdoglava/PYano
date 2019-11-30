import pyglet

class toneButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 675
		self.label = pyglet.text.Label(text, x = xCoord, y = 675, font_size = 32, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def reset():
		pass
	def on(self,x,y):
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
	def on(self,x,y):
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

class chordButton:
	def __init__(self, xCoord, text, buttons, status):
		self.x = xCoord
		self.y = 555
		self.status = status
		self.label = pyglet.text.Label(text, x = xCoord, y = 555, font_size = 30, anchor_x = 'center', anchor_y = 'center', batch = buttons)

	def on(self,x,y):
		if (self.x - 25 <= x <= self.x + 25) and(self.y - 20 <= y<= self.y +20):
			return True
		else:
			return False

def resetChord(keylist, i):
	for x in range(len(keylist)):
		if x != i:
			keylist[x].label.font_size = 30



class playButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 70
		self.label = pyglet.text.Label(text, x = xCoord, y = 70, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 45 <= x <= self.x + 45) and(self.y - 22 <= y<= self.y +22):
			return True
		else:
			return False

class changeButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 70
		self.label = pyglet.text.Label(text, x = xCoord, y = 70, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 85 <= x <= self.x + 85) and(self.y - 22 <= y<= self.y +22):
			return True
		else:
			return False

class instructionsButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 70
		self.label = pyglet.text.Label(text, x = xCoord, y = 70, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 125 <= x <= self.x + 125) and(self.y - 22 <= y<= self.y +22):
			return True
		else:
			return False


class presetButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 70
		self.label = pyglet.text.Label(text, x = xCoord, y = 70, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 15 <= x <= self.x + 15) and(self.y - 22 <= y<= self.y +22):
			return True
		else:
			return False