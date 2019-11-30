import pyglet
import keys
import buttons
import generator
import instructions
import presets

from pyglet.window import mouse

window = pyglet.window.Window(1280, 720, resizable = False)
keyList = keys.getKeys()


#draw labels
labels = pyglet.graphics.Batch()
tonalityLabel = pyglet.text.Label("Tonality", x = 30, y = 675, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
keyLabel = pyglet.text.Label("Key", x = 30, y = 615, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
chordLabel = pyglet.text.Label("Chords", x = 30, y = 555, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
presetsLabel = pyglet.text.Label("Presets:", x = 150, y = 70, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = labels)
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
#draw preset buttons
presetButtonsBatch = pyglet.graphics.Batch()
presetButtons = []
presetButtons.append(buttons.presetButton(300, "1", presetButtonsBatch))
presetButtons.append(buttons.presetButton(370, "2", presetButtonsBatch))
presetButtons.append(buttons.presetButton(440, "3", presetButtonsBatch))
presetButtons.append(buttons.presetButton(510, "4", presetButtonsBatch))

playButton = buttons.playButton(630, "Play", labels)
changeButton = buttons.changeButton(810, "Change", labels)
instructionsButton = buttons.instructionsButton(1090, "Instructions", labels)
#draw load button

#draw preset button

#starting variables
tonalityButtons[0].label.font_size = 40
keyButtons[0].label.font_size = 36

#current tonality, keys, chord, and preset
current = [0,0,-1, -1]

@window.event
def on_draw():
	window.clear()
	for key in keyList:
		key.draw()
	labels.draw()
	toneButtonsBatch.draw()
	keyButtonsBatch.draw()
	chordButtonsBatch.draw()
	presetButtonsBatch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
	print(x,y)
	'''
	HOW TO USE keys.turn
	if button == mouse.LEFT and 181<=x<=241 and 210<=y<=510:
		keys.turn(keyList,[0])
	'''
	for i in range(len(tonalityButtons)):
		if(tonalityButtons[i].on(x,y) and i == current[0]):
			pass
		elif(tonalityButtons[i].on(x,y) and i != current[0]):
			current[0] = i
			current[2] = -1
			buttons.resetTone(tonalityButtons, i)
			tonalityButtons[i].label.font_size = 40
			generator.generateChordList(current,chordButtons)
			keys.turn(keyList,[])

	for i in range(len(keyButtons)):
		if(keyButtons[i].on(x,y) and i == current[1]):
			pass
		elif (keyButtons[i].on(x,y) and i != current[1]):
			current[1] = i
			current[2] = -1
			buttons.resetKey(keyButtons,i)
			keyButtons[i].label.font_size = 36
			generator.generateChordList(current,chordButtons)
			keys.turn(keyList,[])

	for i in range(len(chordButtons)):
		if(chordButtons[i].on(x,y) and i == current[2]):
			#clicked, but is current
			pass
		if(chordButtons[i].on(x,y) and i != current[2]):
			#status is on, this buttons is clicked, but is not current
			current[2] = i
			buttons.resetChord(chordButtons, i)
			chordButtons[i].label.font_size = 38
			keys.turn(keyList,generator.generateChord(current, chordButtons))

	for i in range(len(presetButtons)):
		if(presetButtons[i].on(x,y) and current[3] != i):
			currentPreset = i
			print("Preset " + str(i+1) + " is clicked.")
			presetButtons[i].label.font_size = 46

	if(playButton.on(x,y)):
		print("play is clicked")

	if(changeButton.on(x,y)):
		print("change is clicked")

	if(instructionsButton.on(x,y)):
		print("instruction is clicked")


@window.event
def on_mouse_motion(x, y, button, modifiers): 
	for i in range(len(tonalityButtons)):
		if i!= current[0]:
			if tonalityButtons[i].on(x,y):
				tonalityButtons[i].label.font_size = 36
			else:
				tonalityButtons[i].label.font_size = 32

	for i in range(len(keyButtons)):
		if i!= current[1]:
			if keyButtons[i].on(x,y):
				keyButtons[i].label.font_size = 32
			else:
				keyButtons[i].label.font_size = 28

	for i in range(len(chordButtons)):
		if i!= current[2]:
			if chordButtons[i].on(x,y):
				chordButtons[i].label.font_size = 34
			else:
				chordButtons[i].label.font_size = 30

	for i in range(len(presetButtons)):
		if i != current[3]:
			if presetButtons[i].on(x,y):
				presetButtons[i].label.font_size = 42
			else:
				presetButtons[i].label.font_size = 36

	if(playButton.on(x,y)):
		playButton.label.font_size = 46
	else:		
		playButton.label.font_size = 36

	if(changeButton.on(x,y)):
		changeButton.label.font_size = 46
	else:
		changeButton.label.font_size = 36

	if(instructionsButton.on(x,y)):
		instructionsButton.label.font_size = 46
	else:
		instructionsButton.label.font_size = 36

if __name__ == "__main__":
	pyglet.app.run()