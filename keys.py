import pyglet 

numberOfChords = 0

def getKeys():
	keys = []
	keybatch = pyglet.graphics.Batch()
	
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 181, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 229, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 247, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 295, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 313, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 379, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 427, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 445, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 493, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 511, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 559, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 577, y =210, batch = keybatch))

	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 643, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 691, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 709, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 757, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 775, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 841, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 889, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 907, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 955, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 973, y =210, batch = keybatch))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 1021, y = 306))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 1039, y =210, batch = keybatch))

	return keys

def turn(keylist, turnlist):
	for i in range(len(keylist)):		
		if i in [0,5,12,17]:
			keylist[i].image = pyglet.image.load("whiteA.png")
		if i in [2,7,9,14,19,21]:
			keylist[i].image = pyglet.image.load("whiteB.png")
		if i in [4,11,16,23]:
			keylist[i].image = pyglet.image.load("whiteC.png")
		if i in [1,3,6,8,10,13,15,18,26,22]:
			keylist[i].image = pyglet.image.load("black.png")
	for i in turnlist:
		if i in [0,5,12,17]:
			keylist[i].image = pyglet.image.load("whiteAH.png")
		if i in [2,7,9,14,19,21]:
			keylist[i].image = pyglet.image.load("whiteBH.png")
		if i in [4,11,16,23]:
			keylist[i].image = pyglet.image.load("whiteCH.png")
		if i in [1,3,6,8,10,13,15,18,26,22]:
			keylist[i].image = pyglet.image.load("blackH.png")

def MajorMinor():
	majmin = []									#major/minor (1st layer) labels
	return majmin

def scales():									#2nd layer labels
	scaleList = []
	return scaleList

def showList(listOfChords):						#3rd layer labels
	global numberOfChords
	numberOfChords = len(listOfChords)
	chordList = []

	for i in listOfChords:
		pass
	return chordList