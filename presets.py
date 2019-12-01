def showPreset(presetNumber, thisLabel):	
	file = open("presets.txt", 'r')
	presetList = []
	for i in file:
		j = i.split(' ')
		k = []
		for element in j:
			try:
				k.append(int(element))
			except:
				pass
		presetList.append(k)
	presentPreset = presetList[presetNumber]
	if presentPreset[0] == 0:
		return ("")
	else:
		presentPreset.pop(0)
		tonality = presentPreset.pop(0)
		key = presentPreset.pop(0)
		if tonality == 0:
			tonality = 'Major'
		else:
			tonality = 'Minor'
		key = generator.chordOrder[key]
		returnString = key + ' ' + tonality + ': '
		return(returnString)
	print(presentPreset)
	file.close()

def loadPreset(presetNumber):
	file = open("presets.txt", 'r')
	presetList = []
	for i in file:
		j = i.split(' ')
		k = []
		for element in j:
			k.append(int(element))
		presetList.append(k)
	presentPreset = presetList[presetNumber]
	file.close()
	return presentPreset

def savePreset(presetNumber,newPreset):
	file = open("presets.txt", 'r')
	presetList = []
	for i in file:
		j = i.split(' ')
		k = []
		for element in j:
			k.append(int(element))
		presetList.append(k)
	file.close()
	presetList[presetNumber] = newPreset
	file = open("presets.txt", 'w')
	writeList = []	
	writeString = ''
	for i in presetList:
		for j in range(len(i)):
			i[j] = str(i[j])
		writeString+= ' '.join(i)
		writeString += '\n'
	file.write(writeString)
	file.close()

