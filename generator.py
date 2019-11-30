chordOrder = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
	"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
]

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

	if current[1] > 6 and currentChord > 14:
		currentChord = currentChord % 12
	print(current[1], currentChord)
	for i in progression:
		currentChord += i
		returnList.append(currentChord)

	return returnList