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
			tonelist[x].label.color = (255,255,255,255)

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
			keylist[x].label.color = (255,255,255,255)

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

def resetChord(chordlist, i):
	for x in range(len(chordlist)):
		if x != i:
			chordlist[x].label.font_size = 30
			chordlist[x].label.color = (255,255,255,255)



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


def resetPreset(presetlist, i):
	for x in range(len(presetlist)):
		if x != i:
			presetlist[x].label.font_size = 36
			presetlist[x].label.color = (255,255,255,255)

keyButtonsBatch = pyglet.graphics.Batch()
keyButtons = []
keyButtons.append(keyButton(270, "C", keyButtonsBatch, 0))
keyButtons.append(keyButton(330, "C#", keyButtonsBatch, 1))
keyButtons.append(keyButton(390, "D", keyButtonsBatch, 0))
keyButtons.append(keyButton(450, "D#", keyButtonsBatch, 1))
keyButtons.append(keyButton(510, "E", keyButtonsBatch, 0))
keyButtons.append(keyButton(570, "F", keyButtonsBatch, 0))
keyButtons.append(keyButton(630, "F#", keyButtonsBatch, 1))
keyButtons.append(keyButton(690, "G", keyButtonsBatch, 0))
keyButtons.append(keyButton(750, "G#", keyButtonsBatch, 1))
keyButtons.append(keyButton(810, "A", keyButtonsBatch, 0))
keyButtons.append(keyButton(870, "A#", keyButtonsBatch, 1))
keyButtons.append(keyButton(930, "B", keyButtonsBatch, 0))


toneButtonsBatch = pyglet.graphics.Batch()
tonalityButtons = []
tonalityButtons.append(toneButton(300, "Major", toneButtonsBatch))
tonalityButtons.append(toneButton(450, "Minor", toneButtonsBatch))


chordButtonsBatch = pyglet.graphics.Batch()
chordButtons = []
chordButtons.append(chordButton(270, 'C', chordButtonsBatch, 0))
chordButtons.append(chordButton(370, 'D', chordButtonsBatch, 0))
chordButtons.append(chordButton(470, 'E', chordButtonsBatch, 0))
chordButtons.append(chordButton(570, 'F', chordButtonsBatch, 0))
chordButtons.append(chordButton(670, 'G', chordButtonsBatch, 0))
chordButtons.append(chordButton(770, 'A', chordButtonsBatch, 0))
chordButtons.append(chordButton(870, 'B', chordButtonsBatch, 0))


presetButtonsBatch = pyglet.graphics.Batch()
presetButtons = []
presetButtons.append(presetButton(300, "1", presetButtonsBatch))
presetButtons.append(presetButton(370, "2", presetButtonsBatch))
presetButtons.append(presetButton(440, "3", presetButtonsBatch))
presetButtons.append(presetButton(510, "4", presetButtonsBatch))