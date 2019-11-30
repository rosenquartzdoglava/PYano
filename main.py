import pyglet
import keys
import buttons
import generator
from pyglet.window import mouse

window = pyglet.window.Window(1280, 720, resizable = False)

keyList = keys.getKeys()


#draw labels
labels = pyglet.graphics.Batch()
tonalityLabel = pyglet.text.Label("Tonality", x = 30, y = 675, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
keyLabel = pyglet.text.Label("Key", x = 30, y = 615, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
chordLabel = pyglet.text.Label("Chords", x = 30, y = 555, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)

#draw tone buttons (1st layer): major, minor
toneButtonsBatch = pyglet.graphics.Batch()
tonalityButtons = []
tonalityButtons.append(buttons.toneButton(300, "major", toneButtonsBatch))
tonalityButtons.append(buttons.toneButton(450, "minor", toneButtonsBatch))
#draw key buttons (2nd layer)
keyButtonsBatch = pyglet.graphics.Batch()
keyButtons = []
keyButtons.append(buttons.keyButton(270, "C", keyButtonsBatch, 0))
keyButtons.append(buttons.keyButton(330, "C#", keyButtonsBatch, 1))
keyButtons.append(buttons.keyButton(390, "D", keyButtonsBatch, 0))
keyButtons.append(buttons.keyButton(450, "D#", keyButtonsBatch, 1))
keyButtons.append(buttons.keyButton(510, "E", keyButtonsBatch, 0))
keyButtons.append(buttons.keyButton(570, "F", keyButtonsBatch, 0))
keyButtons.append(buttons.keyButton(630, "F#", keyButtonsBatch, 1))
keyButtons.append(buttons.keyButton(690, "G", keyButtonsBatch, 0))
keyButtons.append(buttons.keyButton(750, "G#", keyButtonsBatch, 1))
keyButtons.append(buttons.keyButton(810, "A", keyButtonsBatch, 0))
keyButtons.append(buttons.keyButton(870, "A#", keyButtonsBatch, 1))
keyButtons.append(buttons.keyButton(930, "B", keyButtonsBatch, 0))
#draw chord buttons (3rd layer)
chordButtonsBatch = pyglet.graphics.Batch()
chordButtons = []
chordButtons.append(buttons.chordButton(270, 'C', chordButtonsBatch, 0))
chordButtons.append(buttons.chordButton(370, 'D', chordButtonsBatch, 0))
chordButtons.append(buttons.chordButton(470, 'E', chordButtonsBatch, 0))
chordButtons.append(buttons.chordButton(570, 'F', chordButtonsBatch, 0))
chordButtons.append(buttons.chordButton(670, 'G', chordButtonsBatch, 0))
chordButtons.append(buttons.chordButton(770, 'A', chordButtonsBatch, 0))
chordButtons.append(buttons.chordButton(870, 'B', chordButtonsBatch, 0))


#starting variables
tonalityButtons[0].label.font_size = 40
keyButtons[0].label.font_size = 36

#current tonality, keys, and chord
current = [0,0,-1]

@window.event
def on_draw():
	window.clear()
	for key in keyList:
		key.draw()
	labels.draw()
	toneButtonsBatch.draw()
	keyButtonsBatch.draw()
	chordButtonsBatch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
	'''
	HOW TO USE keys.turn
	if button == mouse.LEFT and 181<=x<=241 and 210<=y<=510:
		keys.turn(keyList,[0])
	'''
	for i in range(len(tonalityButtons)):
		if(tonalityButtons[i].onclick(x,y) and i == current[0]):
			pass
		elif(tonalityButtons[i].onclick(x,y) and i != current[0]):
			current[0] = i
			current[2] = -1
			buttons.resetTone(tonalityButtons, i)
			tonalityButtons[i].label.font_size = 40
			generator.generateChordList(current,chordButtons)
			keys.turn(keyList,[])

	for i in range(len(keyButtons)):
		if(keyButtons[i].onclick(x,y) and i == current[1]):
			pass
		elif (keyButtons[i].onclick(x,y) and i != current[1]):
			current[1] = i
			current[2] = -1
			buttons.resetKey(keyButtons,i)
			keyButtons[i].label.font_size = 36
			generator.generateChordList(current,chordButtons)
			keys.turn(keyList,[])

	for i in range(len(chordButtons)):
		if(chordButtons[i].onclick(x,y) and i == current[2]):
			#clicked, but is current
			pass
		if(chordButtons[i].onclick(x,y) and i != current[2]):
			#status is on, this buttons is clicked, but is not current
			current[2] = i
			buttons.resetChord(chordButtons, i)
			chordButtons[i].label.font_size = 38
			keys.turn(keyList,generator.generateChord(current, chordButtons))

@window.event
def on_mouse_motion(x, y, button, modifiers): 
	for i in range(len(tonalityButtons)):
		if i!= current[0]:
			if tonalityButtons[i].hover(x,y):
				tonalityButtons[i].label.font_size = 36
			else:
				tonalityButtons[i].label.font_size = 32

	for i in range(len(keyButtons)):
		if i!= current[1]:
			if keyButtons[i].hover(x,y):
				keyButtons[i].label.font_size = 32
			else:
				keyButtons[i].label.font_size = 28

	for i in range(len(chordButtons)):
		if i!= current[2]:
			if chordButtons[i].hover(x,y):
				chordButtons[i].label.font_size = 34
			else:
				chordButtons[i].label.font_size = 30

pyglet.app.run()