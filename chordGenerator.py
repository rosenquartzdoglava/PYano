chordOrder = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
	"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
]
toneOrder = ["Major", "Minor"]

def generateChordList(current, chordButtons):
	if current[0] == 0: #tonality is major
		formula = [0,2,2,1,2,2,2]
	else: #tonality is minor
		formula = [0,2,1,2,2,1,2]

	currentChord = current[1]
	returnList = []

	for i in formula:
		currentChord+=i
		returnList.append(chordOrder[currentChord])

	for i in range(len(chordButtons)):
		chordButtons[i].label.text = returnList[i]

	return returnList

def generateChord(current, chordButtons):
	if current[0] == 0: #tonality is major
		formula = [0,2,2,1,2,2,2]	
		chordFormula= [0,1,1,0,0,1,2]

	else: #tonality is minor
		formula = [0,2,1,2,2,1,2]
		chordFormula = [1,2,0,1,1,0,0]

	if chordFormula[current[2]] == 0: # chord is a major chord
		progression = [0,4,3]
	elif chordFormula[current[2]] == 1:
		progression = [0,3,4]
	elif chordFormula[current[2]] == 2:
		progression = [0,3,3]

	returnList = []
	currentChord = current[1]

	for i in range(current[2]+1):
		currentChord += formula[i]

	for i in progression:
		currentChord += i
		returnList.append(currentChord)

	return returnList

def presetDescription(presetList):
	tonality = presetList.pop(0)
	key = presetList.pop(0)
	baseKey = key
	if tonality == 0:
		formula = [0,2,2,1,2,2,2]
		tonality = 'Major'
	else:
		formula = [0,2,1,2,2,1,2]
		tonality = 'Minor'

	keyChordList = []
	for i in formula:
		key+=i
		keyChordList.append(key)

	returnList = []
	for i in presetList:
		returnList.append(chordOrder[keyChordList[i]])

	returnString = chordOrder[baseKey] + ' ' + tonality + ' : '
	returnString += ' - '.join(returnList)
	return returnString

def generatePreset(presetList):
	tonality = presetList.pop(0)
	key = presetList.pop(0)

	if tonality == 0:
		formula = [0,2,2,1,2,2,2]
		chordFormula= [0,1,1,0,0,1,2]
		tonality = 'Major'
	else: #tonality is minor
		formula = [0,2,1,2,2,1,2]
		chordFormula = [1,2,0,1,1,0,0]
		tonality = 'Minor'

	keyChordList = []
	for i in formula:
		key+=i
		keyChordList.append(key)

	chordProgressions = []
	progressionFormulas = [[0,4,3],[0,3,4],[0,3,3]]

	for i in range(len(keyChordList)):
		tempList = []
		tempSum = keyChordList[i]
		for j in progressionFormulas[chordFormula[i]]:
			tempSum+=j
			tempList.append(tempSum)
		chordProgressions.append(tempList)

	returnList = []
	for i in presetList:
		returnList.append(chordProgressions[i])
		
	returnList.append([])
	return returnList
	#returns a list of variables to be passed into keys.turnList