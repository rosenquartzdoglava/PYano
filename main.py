import pyglet
import keys
import buttons
import presets
import chordGenerator
import copy
from pyglet.window import mouse

window = pyglet.window.Window(1280, 720, resizable = False)
keyList = keys.getKeys()

labels = pyglet.graphics.Batch()
toneButtonsBatch = buttons.toneButtonsBatch
keyButtonsBatch = buttons.keyButtonsBatch
chordButtonsBatch = buttons.chordButtonsBatch
presetButtonsBatch = buttons.presetButtonsBatch


tonalityButtons = buttons.tonalityButtons
keyButtons = buttons.keyButtons
chordButtons = buttons.chordButtons
presetButtons = buttons.presetButtons

tonalityLabel = pyglet.text.Label("Tonality", x = 30, y = 675, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
keyLabel = pyglet.text.Label("Key", x = 30, y = 615, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
chordLabel = pyglet.text.Label("Chords", x = 30, y = 555, font_size = 36, anchor_x ='left', anchor_y = 'center', batch = labels)
presetsLabel = pyglet.text.Label("Presets:", x = 150, y = 70, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = labels)
currentPresetLabel = pyglet.text.Label("No presets loaded.", x = 640, y = 150, font_size = 36, anchor_x = 'center', anchor_y = 'center', batch = labels)
playButton = buttons.playButton(630, "Play", labels)
changeButton = buttons.changeButton(810, "Change", labels)

tonalityButtons[0].label.font_size = 40
tonalityButtons[0].label.color = (200, 200, 127, 255)
keyButtons[0].label.font_size = 36
keyButtons[0].label.color = (200, 200, 127, 255)
current = [0,0,-1, -1, -1] #tonality, key, chord, current Preset Loaded, current Preset being changed
presetChords = []
currentTime = 0
isReady = 0
currentPreset = [1,0,0]
presetData = []
presetIsLoaded = 0

def update(dt):
	global presetChords
	global currentTime
	print('ahm')
	currentTime += 1
	if currentTime + 1 < len(presetData):
		buttons.resetChord(chordButtons, presetData[currentTime+1])
		chordButtons[presetData[currentTime + 1]].label.font_size = 38
		chordButtons[presetData[currentTime + 1]].label.color = (200,200,127,255)
	else:
		buttons.resetChord(chordButtons, -1)
	keys.turn(keyList, presetChords[currentTime -1])

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
	global presetChords
	global currentTime
	global isReady
	global currentPreset
	global current
	global presetData
	global presetIsLoaded
	'''
	HOW TO USE keys.turn
	if button == mouse.LEFT and 181<=x<=241 and 210<=y<=510:
		keys.turn(keyList,[0])
	'''
	if current[4] == -1:
		for i in range(len(tonalityButtons)):
			if(tonalityButtons[i].on(x,y) and i == current[0]):
				pass
			elif(tonalityButtons[i].on(x,y) and i != current[0]):
				current[0] = i
				current[2] = -1
				buttons.resetTone(tonalityButtons, i)
				tonalityButtons[i].label.font_size = 40
				tonalityButtons[i].label.color = (200, 200, 127, 255)
				chordGenerator.generateChordList(current,chordButtons)
				keys.turn(keyList,[])

		for i in range(len(keyButtons)):
			if(keyButtons[i].on(x,y) and i == current[1]):
				pass
			elif (keyButtons[i].on(x,y) and i != current[1]):
				current[1] = i
				current[2] = -1
				buttons.resetKey(keyButtons,i)
				keyButtons[i].label.font_size = 36
				keyButtons[i].label.color =  (200, 200, 127, 255)
				chordGenerator.generateChordList(current,chordButtons)
				keys.turn(keyList,[])

		for i in range(len(chordButtons)):
			if(chordButtons[i].on(x,y) and i == current[2]):
				current[2] = -1
				keys.turn(keyList,[])
				buttons.resetChord(chordButtons, -1)

			elif(chordButtons[i].on(x,y) and i != current[2]):
				#status is on, this buttons is clicked, but is not current
				current[2] = i
				buttons.resetChord(chordButtons, i)
				chordButtons[i].label.font_size = 38
				chordButtons[i].label.color =  (200, 200, 127, 255)
				keys.turn(keyList,chordGenerator.generateChord(current, chordButtons))

		for i in range(len(presetButtons)):
			if(presetButtons[i].on(x,y) and current[3] != i):
				buttons.resetPreset(presetButtons, i)
				current[3] = i
				presetList = presets.loadPreset(i)
				presetIsLoaded = 1
				isReady = presetList.pop(0)
				presetListA = copy.copy(presetList)
				presetListB = copy.copy(presetList)

				if isReady:
					currentPresetLabel.text = chordGenerator.presetDescription(presetListA)
					presetChords = chordGenerator.generatePreset(presetListB)
					presetData = presetList
				else:
					currentPresetLabel.text = "This preset is empty."
				presetButtons[i].label.font_size = 52
				presetButtons[i].label.color =  (200, 200, 127, 255)

			elif presetButtons[i].on(x,y) and current[3] == i:
				buttons.resetPreset(presetButtons,-1)
				current[3] = -1
				isReady = 0
				currentPresetLabel.text = "No preset loaded."
				presetIsLoaded = 0

		if(playButton.on(x,y) and isReady):
			currentTime = 0
			print("play is clicked")
			times = []
			print(presetData)
			buttons.resetKey(keyButtons,presetData[1])
			keyButtons[presetData[1]].label.font_size = 36
			keyButtons[presetData[1]].label.color = (200,200,127,255)
			buttons.resetTone(tonalityButtons,presetData[0])
			tonalityButtons[presetData[0]].label.font_size = 40
			tonalityButtons[presetData[0]].label.color = (200,200,127,255)
			current[0] = presetData[0]
			current[1] = presetData[1]
			chordGenerator.generateChordList(current,chordButtons)

			for j in range(len(presetChords)):
				times.append(1.5*j)
			for j in times:
				pyglet.clock.schedule_once(update,j)

		if(changeButton.on(x,y)):
			currentPreset = [1, current[0], current[1]]
			changeButton.label.text = 'Save'
			currentPresetLabel.text = 'Editing Preset ' +str(current[3]+1) + ': ' +chordGenerator.chordOrder[currentPreset[2]] +' ' + chordGenerator.toneOrder[currentPreset[1]]
			currentPresetLabel.font_size = 28
			buttons.resetKey(keyButtons,currentPreset[2])
			keyButtons[currentPreset[2]].label.font_size = 36
			buttons.resetTone(tonalityButtons,currentPreset[1])
			tonalityButtons[currentPreset[1]].label.font_size = 40
			buttons.resetChord(chordButtons, -1) 
			keys.turn(keyList, [])
			isReady = 0	
			current[4] = current[3]

	else: #change has been clicked and is ongoing
		for i in range(len(tonalityButtons)):
			if(tonalityButtons[i].on(x,y) and i == current[0]):
				pass
			elif(tonalityButtons[i].on(x,y) and i != current[0]):
				current[0] = i
				current[2] = -1
				buttons.resetTone(tonalityButtons, i)
				tonalityButtons[i].label.font_size = 40
				chordGenerator.generateChordList(current,chordButtons)
				keys.turn(keyList,[])
				currentPreset[1] = i
				currentPreset = currentPreset[:3]
				currentPresetLabel.text = 'Editing Preset ' +str(current[3]+1) + ': ' +chordGenerator.chordOrder[currentPreset[2]] +' ' + chordGenerator.toneOrder[currentPreset[1]]

		for i in range(len(keyButtons)):
			if(keyButtons[i].on(x,y) and i == current[1]):
				pass
			elif (keyButtons[i].on(x,y) and i != current[1]):
				current[1] = i
				current[2] = -1
				buttons.resetKey(keyButtons,i)
				keyButtons[i].label.font_size = 36
				chordGenerator.generateChordList(current,chordButtons)
				keys.turn(keyList,[])
				currentPreset[2] = i
				currentPreset = currentPreset[:3]
				currentPresetLabel.text = 'Editing Preset ' +str(current[3]+1) + ': ' +chordGenerator.chordOrder[currentPreset[2]] +' ' + chordGenerator.toneOrder[currentPreset[1]]

		for i in range(len(chordButtons)):
			if(chordButtons[i].on(x,y) and i == current[2]):
				#clicked, but is current
				pass
			if(chordButtons[i].on(x,y) and i != current[2]):
				#status is on, this buttons is clicked, but is not current
				current[2] = i
				buttons.resetChord(chordButtons, i)
				chordButtons[i].label.font_size = 38
				keys.turn(keyList,chordGenerator.generateChord(current, chordButtons))
				currentPreset.append(i)
				currentPresetLabel.text += ' - ' + chordButtons[i].label.text
				print(currentPreset)

		if(changeButton.on(x,y)):
			print("change is clicked")
			print(currentPreset[2])
			for i in currentPreset:
				print(type(i))
			presets.savePreset(current[3],currentPreset)
			current[4] = -1
			buttons.resetChord(chordButtons, -1) 
			currentPresetLabel.text = 'No preset loaded.'
			changeButton.label.text = 'Change'
			buttons.resetPreset[presetButtons,-1]
			keys.turn(keyList, [])

@window.event
def on_mouse_motion(x, y, button, modifiers): 
	for i in range(len(tonalityButtons)):
		if i!= current[0]:
			if tonalityButtons[i].on(x,y):
				tonalityButtons[i].label.font_size = 40
			else:
				tonalityButtons[i].label.font_size = 32

	for i in range(len(keyButtons)):
		if i!= current[1]:
			if keyButtons[i].on(x,y):
				keyButtons[i].label.font_size = 36
			else:
				keyButtons[i].label.font_size = 28

	for i in range(len(chordButtons)):
		if i!= current[2]:
			if chordButtons[i].on(x,y):
				chordButtons[i].label.font_size = 38
			else:
				chordButtons[i].label.font_size = 30

	for i in range(len(presetButtons)):
		if i != current[3]:
			if presetButtons[i].on(x,y):
				presetButtons[i].label.font_size = 52
			else:
				presetButtons[i].label.font_size = 36

	if(playButton.on(x,y) and presetIsLoaded):
		playButton.label.font_size = 46
	elif playButton.on(x,y) and not presetIsLoaded:		
		playButton.label.font_size = 36
		playButton.label.color = (255,0,0,255)
	else:
		playButton.label.font_size = 36
		playButton.label.color = (255,255,255,255)


	if(changeButton.on(x,y) and presetIsLoaded):
		changeButton.label.font_size = 52
	elif changeButton.on(x,y) and not presetIsLoaded:	
		changeButton.label.font_size = 36
		changeButton.label.color = (255,0,0,255)
	else:
		changeButton.label.font_size = 36
		changeButton.label.color = (255,255,255,255)

if __name__ == "__main__":
	pyglet.app.run()