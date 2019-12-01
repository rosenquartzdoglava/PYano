import pyglet
import keys
import buttons
import presets
import chordGenerator
import copy
from pyglet.window import mouse
from pyglet import font

window = pyglet.window.Window(1280, 720, resizable = False)
keyList = keys.getKeys()
font.add_file('montserrat semibold.otf')

labels = pyglet.graphics.Batch()
toneButtonsBatch = buttons.toneButtonsBatch
keyButtonsBatch = buttons.keyButtonsBatch
chordButtonsBatch = buttons.chordButtonsBatch
presetButtonsBatch = buttons.presetButtonsBatch
speedButtonsBatch = buttons.speedButtonsBatch

tonalityButtons = buttons.tonalityButtons
keyButtons = buttons.keyButtons
chordButtons = buttons.chordButtons
presetButtons = buttons.presetButtons
speedButtons = buttons.speedButtons

logo = pyglet.sprite.Sprite(pyglet.image.load("logo.png"), x = 25, y = 615, batch = labels)
tonalityLabel = pyglet.text.Label("TONALITY", x = 70, y = 605, font_name = 'Montserrat SemiBold', font_size = 24, color = (218,240,37,255), anchor_x ='left', anchor_y = 'center', batch = labels)
keyLabel = pyglet.text.Label("KEY", x = 70, y = 550, font_name = 'Montserrat SemiBold', font_size = 24, color = (218,240,37,255), anchor_x ='left', anchor_y = 'center', batch = labels)
chordLabel = pyglet.text.Label("CHORD", x = 70, y = 495, font_name = 'Montserrat SemiBold', font_size = 24, color = (218,240,37,255), anchor_x ='left', anchor_y = 'center', batch = labels)
presetsLabel = pyglet.text.Label("Presets:", x = 60, y = 35, font_name = 'Montserrat SemiBold', font_size = 24, anchor_x = 'left', anchor_y = 'center', batch = labels)
speedLabel = pyglet.text.Label("Speed:", x = 490, y = 35, font_name = 'Montserrat SemiBold', font_size = 24, anchor_x = 'left', anchor_y = 'center', batch = labels)
currentPresetLabel = pyglet.text.Label("", x = 630, y = 85, font_name = 'Montserrat',italic = True, font_size = 24, anchor_x = 'center', anchor_y = 'center', batch = labels)
playButton = buttons.playButton(930, "Play", labels)
changeButton = buttons.changeButton(1120, "Change", labels)

tonalityButtons[0].label.font_size = 24
tonalityButtons[0].label.color = (200, 200, 127, 255)
keyButtons[0].label.font_size = 24
keyButtons[0].label.color = (200, 200, 127, 255)
current = [0, 0, -1, -1, 1, 0, 0, -1] #tonality button, key button, chord button, preset button, preset Status, preset Loaded?, is playing, current speed Button
presetChords = []
currentTime = 0
currentPreset = [1,0,0]
presetData = []

def updateChords(dt):
	global current
	global presetChords
	global currentTime
	currentTime += 1
	if currentTime + 1 < len(presetData):
		buttons.resetChord(chordButtons, presetData[currentTime+1])
		chordButtons[presetData[currentTime + 1]].label.font_size = 30
		chordButtons[presetData[currentTime + 1]].label.color = (200,200,127,255)
	else:
		buttons.resetChord(chordButtons, -1)
		#change play button color
		playButton.label.font_size = 24
		playButton.label.color = (255,255,255,255)
		current[6] = 0
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
	speedButtonsBatch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
	global presetChords
	global currentTime
	global currentPreset
	global current
	global presetData

	if not current[6]:
		if current[4]:
			for i in range(len(tonalityButtons)):
				if(tonalityButtons[i].on(x,y) and i != current[0]):
					current[0] = i
					current[2] = -1
					buttons.resetTone(tonalityButtons, i)
					tonalityButtons[i].label.font_size = 24
					tonalityButtons[i].label.color = (200, 200, 127, 255)
					chordGenerator.generateChordList(current,chordButtons)
					keys.turn(keyList,[])

			for i in range(len(keyButtons)):
				if (keyButtons[i].on(x,y) and i != current[1]):
					current[1] = i
					current[2] = -1
					buttons.resetKey(keyButtons,i)
					keyButtons[i].label.font_size = 24
					keyButtons[i].label.color =  (200, 200, 127, 255)
					chordGenerator.generateChordList(current,chordButtons)
					keys.turn(keyList,[])

			for i in range(len(chordButtons)):
				if(chordButtons[i].on(x,y) and i == current[2]):
					current[2] = -1
					buttons.resetChord(chordButtons, -1)
					keys.turn(keyList,[])
				elif(chordButtons[i].on(x,y) and i != current[2]):
					#status is on, this buttons is clicked, but is not current
					current[2] = i
					buttons.resetChord(chordButtons, i)
					chordButtons[i].label.font_size = 24
					chordButtons[i].label.color =  (200, 200, 127, 255)
					keys.turn(keyList,chordGenerator.generateChord(current, chordButtons))

			for i in range(len(presetButtons)):
				if presetButtons[i].on(x,y) and current[3] != i:
					current[3] = i
					buttons.resetPreset(presetButtons, i)
					presetButtons[i].label.font_size = 24
					presetButtons[i].label.color =  (200, 200, 127, 255)
					presetList = presets.loadPreset(i)
					current[5] = presetList.pop(0)
					presetListA = copy.copy(presetList)
					presetListB = copy.copy(presetList)
					if current[5]:
						currentPresetLabel.text = chordGenerator.presetDescription(presetListA)
						presetChords = chordGenerator.generatePreset(presetListB)
						presetData = presetList
						buttons.resetSpeed(speedButtons,0)
						speedButtons[0].label.color = (200, 200, 127, 255)
						current[7] = 0
					else:
						buttons.resetSpeed(speedButtons,-1)
						current[7] = -1
						currentPresetLabel.text = "This preset is empty."
				elif presetButtons[i].on(x,y) and current[3] == i:
					buttons.resetPreset(presetButtons,-1)
					current[3] = -1
					current[5] = 0
					currentPresetLabel.text = ""
					current[7] = -1
					buttons.resetSpeed(speedButtons,-1)

			if(playButton.on(x,y) and current[5]):
				currentTime = 0
				times = []
				current[0] = presetData[0]
				current[1] = presetData[1]
				current[2] = -1
				current[6] = 1
				buttons.resetTone(tonalityButtons,presetData[0])
				tonalityButtons[presetData[0]].label.font_size = 24
				tonalityButtons[presetData[0]].label.color = (200,200,127,255)
				buttons.resetKey(keyButtons,presetData[1])
				keyButtons[presetData[1]].label.font_size = 24
				keyButtons[presetData[1]].label.color = (200,200,127,255)
				chordGenerator.generateChordList(current,chordButtons)
				playButton.label.color = (0,0,255,255)
				for j in range(len(presetChords)):
					times.append(j * 3/(current[7]+1))
				for j in times:
					pyglet.clock.schedule_once(updateChords,j)

			if(changeButton.on(x,y)):
				currentPreset = [1, current[0], current[1]]
				changeButton.label.text = 'Save'
				currentPresetLabel.text = 'Clear Preset'
				currentPresetLabel.font_size = 24
				buttons.resetKey(keyButtons,currentPreset[2])
				keyButtons[currentPreset[2]].label.font_size = 24
				buttons.resetTone(tonalityButtons,currentPreset[1])
				tonalityButtons[currentPreset[1]].label.font_size = 24
				buttons.resetChord(chordButtons, -1) 
				buttons.resetSpeed(speedButtons, -1)
				current[7] = -1
				current[2] = -1
				keys.turn(keyList, [])
				current[5] = 0	
				current[4] = 0

			for i in range(len(speedButtons)):
				if speedButtons[i].on(x,y) and i!= current[7] and current[3] != -1:
					current[7] = i
					buttons.resetSpeed(speedButtons, i)
					speedButtons[i].label.color = (200, 200, 127, 255)
					speedButtons[i].label.font_size = 24

		elif len(currentPreset) < 12: #change has been clicked and is ongoing
			for i in range(len(tonalityButtons)):
				if(tonalityButtons[i].on(x,y) and i == current[0]):
					pass
				elif(tonalityButtons[i].on(x,y) and i != current[0]):
					current[0] = i
					current[2] = -1
					buttons.resetTone(tonalityButtons, i)
					tonalityButtons[i].label.font_size = 24
					tonalityButtons[i].label.color = (200,200,127,255)
					chordGenerator.generateChordList(current,chordButtons)
					keys.turn(keyList,[])
					currentPreset[1] = i
					currentPreset = currentPreset[:3]
					currentPresetLabel.text = 'Clear Preset'
			for i in range(len(keyButtons)):
				if(keyButtons[i].on(x,y) and i == current[1]):
					pass
				elif (keyButtons[i].on(x,y) and i != current[1]):
					current[1] = i
					current[2] = -1
					buttons.resetKey(keyButtons,i)
					keyButtons[i].label.color = (200,200,127,255)
					keyButtons[i].label.font_size = 24
					chordGenerator.generateChordList(current,chordButtons)
					keys.turn(keyList,[])
					currentPreset[2] = i
					currentPreset = currentPreset[:3]
					currentPresetLabel.text = "Clear Preset"

			for i in range(len(chordButtons)):
				if(chordButtons[i].on(x,y) and i != current[2]):
					#status is on, this buttons is clicked, but is not current
					current[2] = i
					buttons.resetChord(chordButtons, i)
					chordButtons[i].label.color = (200,200,127,255)
					chordButtons[i].label.font_size = 24
					keys.turn(keyList,chordGenerator.generateChord(current, chordButtons))
					if len(currentPreset) == 3:
						currentPresetLabel.text = 'Editing Preset ' +str(current[3]+1) + ': ' +chordGenerator.chordOrder[currentPreset[2]] +' ' + chordGenerator.toneOrder[currentPreset[1]]
					currentPreset.append(i)
					currentPresetLabel.text += ' - ' + chordButtons[i].label.text
			if(changeButton.on(x,y)):
				if len(currentPreset)>3:
					presets.savePreset(current[3],currentPreset)
				else:
					presets.savePreset(current[3],[0])
				current[3] = -1
				current[4] = 1
				buttons.resetChord(chordButtons, -1) 
				currentPresetLabel.text = ''
				changeButton.label.text = 'Change'
				buttons.resetPreset(presetButtons,-1)
				keys.turn(keyList, [])
		else:			
			if(changeButton.on(x,y)):
				if len(currentPreset)>3:
					presets.savePreset(current[3],currentPreset)
				else:
					presets.savePreset(current[3],[0])
				current[3] = -1
				current[4] = 1
				buttons.resetChord(chordButtons, -1) 
				currentPresetLabel.text = ''
				changeButton.label.text = 'Change'
				buttons.resetPreset(presetButtons,-1)
				keys.turn(keyList, [])

@window.event
def on_mouse_motion(x, y, button, modifiers): 

	if not current[6]:
		for i in range(len(tonalityButtons)):
			if i!= current[0]:
				if tonalityButtons[i].on(x,y):
					tonalityButtons[i].label.font_size = 30
				else:
					tonalityButtons[i].label.font_size = 24

		for i in range(len(keyButtons)):
			if i!= current[1]:
				if keyButtons[i].on(x,y):
					keyButtons[i].label.font_size = 30
				else:
					keyButtons[i].label.font_size = 24

		for i in range(len(chordButtons)):
			if i!= current[2]:
				if chordButtons[i].on(x,y):
					chordButtons[i].label.font_size = 30
				else:
					chordButtons[i].label.font_size = 24

		for i in range(len(presetButtons)):
			if i != current[3]:
				if presetButtons[i].on(x,y):
					presetButtons[i].label.font_size = 30
				else:
					presetButtons[i].label.font_size = 24

		if playButton.on(x,y) and current[5]:
			playButton.label.font_size = 30
		elif playButton.on(x,y) and not current[5]:		
			playButton.label.font_size = 24
			playButton.label.color = (163,39,39,255)
		else:
			playButton.label.font_size = 24
			playButton.label.color = (255,255,255,255)


		if changeButton.on(x,y) and not(current[3] == -1):
			changeButton.label.font_size = 30
		elif changeButton.on(x,y) and (current[3] == -1):	
			changeButton.label.font_size = 24
			changeButton.label.color = (163,39,39,255)
		else:
			changeButton.label.font_size = 24
			changeButton.label.color = (255,255,255,255)

		for i in range(len(speedButtons)):
			if speedButtons[i].on(x,y) and current[5] and i!= current[7]:
				speedButtons[i].label.font_size = 30
				#the buttons should be availble; if it is not current, it becomes bigger. if it is current, nothing happens
			elif speedButtons[i].on(x,y) and not current[5]:
				speedButtons[i].label.font_size = 24
				speedButtons[i].label.color = (162,39,39,255)
				# should become red
			elif current[7] != i:
				speedButtons[i].label.font_size = 24
				speedButtons[i].label.color = (255,255,255,255)
				#turn white

if __name__ == "__main__":
	pyglet.app.run()


'''
things to do
make sure no empty presets
make sure if preset is empty before changing preset is sasved as empty
spread out ui
make information txt file
x1 speed = every 3 seconds
x 1.5 speed = every 2 seconds
x 2 speed = every 1.5 sesconds
x 3 speed = every second
x 4 speed = every 
'''