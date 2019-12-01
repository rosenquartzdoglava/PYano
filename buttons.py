import pyglet
from pyglet import font
font.add_file('montserrat regular.otf')

class toneButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 605
		self.label = pyglet.text.Label(text, x = xCoord, y = 605, font_name = 'Montserrat', font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def reset():
		pass
	def on(self,x,y):
		if (self.x - 50 <= x <= self.x + 50) and(self.y - 15 <= y<= self.y +25):
			return True
		else:
			return False

def resetTone(tonelist, i):
	for x in range(len(tonelist)):
		if x != i:
			tonelist[x].label.font_size = 24
			tonelist[x].label.color = (255,255,255,255)

class keyButton():
	def __init__(self, xCoord, text, buttons, type):
		self.x = xCoord
		self.y = 550
		self.type = type # how large is 
		self.label = pyglet.text.Label(text, x = xCoord, y = 550, font_name = 'Montserrat', font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def reset():
		pass
	def on(self,x,y):
		if self.type == 0:
			if (self.x - 15 <= x <= self.x + 15) and(self.y - 15 <= y<= self.y + 25):
				return True
			else:
				return False
		else:
			if (self.x - 25 <= x <= self.x + 25) and(self.y - 15 <= y<= self.y + 25):
				return True
			else:
				return False

def resetKey(keylist, i):
	for x in range(len(keylist)):
		if x != i:
			keylist[x].label.font_size = 24
			keylist[x].label.color = (255,255,255,255)

class chordButton():
	def __init__(self, xCoord, text, buttons, status):
		self.x = xCoord
		self.y = 495
		self.status = status
		self.label = pyglet.text.Label(text, x = xCoord, y = 495, font_name = 'Montserrat', font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = buttons)

	def on(self,x,y):
		if (self.x - 25 <= x <= self.x + 25) and(self.y - 15 <= y<= self.y + 25):
			return True
		else:
			return False

def resetChord(chordlist, i):
	for x in range(len(chordlist)):
		if x != i:
			chordlist[x].label.font_size = 24
			chordlist[x].label.color = (255,255,255,255)



class playButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 35
		self.label = pyglet.text.Label(text, x = xCoord, y = 33, font_name = 'Montserrat', font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 45 <= x <= self.x + 45) and(self.y - 15 <= y<= self.y +25):
			return True
		else:
			return False

class changeButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 35
		self.label = pyglet.text.Label(text, x = xCoord, y = 33, font_name = 'Montserrat', font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 85 <= x <= self.x + 85) and(self.y - 15 <= y<= self.y +25):
			return True
		else:
			return False

class presetButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 30
		self.label = pyglet.text.Label(text, x = xCoord, y = 32, font_name = 'Montserrat', font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 15 <= x <= self.x + 15) and(self.y - 15 <= y<= self.y +25):
			return True
		else:
			return False

def resetPreset(presetlist, i):
	for x in range(len(presetlist)):
		if x != i:
			presetlist[x].label.font_size = 24
			presetlist[x].label.color = (255,255,255,255)

class speedButton():
	def __init__(self, xCoord, text, buttons):
		self.x = xCoord
		self.y = 30
		self.label = pyglet.text.Label(text, x = xCoord, y = 32, font_name = 'Montserrat', font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = buttons)
	def on(self,x,y):
		if (self.x - 15 <= x <= self.x + 15) and(self.y - 15 <= y<= self.y +25):
			return True
		else:
			return False


def resetSpeed(speedlist, i):
	for x in range(len(speedlist)):
		if x != i:
			speedlist[x].label.font_size = 24
			speedlist[x].label.color = (255,255,255,255)

toneButtonsBatch = pyglet.graphics.Batch()
tonalityButtons = []
tonalityButtons.append(toneButton(330, "Major", toneButtonsBatch))
tonalityButtons.append(toneButton(540, "Minor", toneButtonsBatch))

keyButtonsBatch = pyglet.graphics.Batch()
keyButtons = []
keyButtons.append(keyButton(295, "C", keyButtonsBatch, 0))
keyButtons.append(keyButton(365, "C#", keyButtonsBatch, 1))
keyButtons.append(keyButton(435, "D", keyButtonsBatch, 0))
keyButtons.append(keyButton(505, "D#", keyButtonsBatch, 1))
keyButtons.append(keyButton(575, "E", keyButtonsBatch, 0))
keyButtons.append(keyButton(645, "F", keyButtonsBatch, 0))
keyButtons.append(keyButton(715, "F#", keyButtonsBatch, 1))
keyButtons.append(keyButton(785, "G", keyButtonsBatch, 0))
keyButtons.append(keyButton(855, "G#", keyButtonsBatch, 1))
keyButtons.append(keyButton(925, "A", keyButtonsBatch, 0))
keyButtons.append(keyButton(995, "A#", keyButtonsBatch, 1))
keyButtons.append(keyButton(1065, "B", keyButtonsBatch, 0))

chordButtonsBatch = pyglet.graphics.Batch()
chordButtons = []
chordButtons.append(chordButton(295, 'C', chordButtonsBatch, 0))
chordButtons.append(chordButton(400, 'D', chordButtonsBatch, 0))
chordButtons.append(chordButton(505, 'E', chordButtonsBatch, 0))
chordButtons.append(chordButton(610, 'F', chordButtonsBatch, 0))
chordButtons.append(chordButton(715, 'G', chordButtonsBatch, 0))
chordButtons.append(chordButton(820, 'A', chordButtonsBatch, 0))
chordButtons.append(chordButton(925, 'B', chordButtonsBatch, 0))

presetButtonsBatch = pyglet.graphics.Batch()
presetButtons = []
presetButtons.append(presetButton(230, "1", presetButtonsBatch))
presetButtons.append(presetButton(290, "2", presetButtonsBatch))
presetButtons.append(presetButton(350, "3", presetButtonsBatch))
presetButtons.append(presetButton(410, "4", presetButtonsBatch))

speedButtonsBatch = pyglet.graphics.Batch()
speedButtons = []
speedButtons.append(presetButton(650, "x1", speedButtonsBatch))
speedButtons.append(presetButton(715, "x2", speedButtonsBatch))
speedButtons.append(presetButton(780, "x3", speedButtonsBatch))