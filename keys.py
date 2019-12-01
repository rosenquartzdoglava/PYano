import pyglet 

def getKeys():
	keys = []
	
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 71, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 125, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 153, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 207, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 235, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 317, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 371, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 399, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 453, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 481, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 535, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 563, y =135))

	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 645, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 699, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 727, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 781, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 809, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteA.png"), x = 891, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 945, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 973, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 1027, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteB.png"), x = 1055, y =135))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("black.png"), x = 1109, y = 210))
	keys.append(pyglet.sprite.Sprite(pyglet.image.load("whiteC.png"), x = 1137, y =135))

	return keys

def turn(keylist, turnlist):
	for i in range(len(keylist)):		
		if i in [0,5,12,17]:
			keylist[i].image = pyglet.image.load("whiteA.png")
		if i in [2,7,9,14,19,21]:
			keylist[i].image = pyglet.image.load("whiteB.png")
		if i in [4,11,16,23]:
			keylist[i].image = pyglet.image.load("whiteC.png")
		if i in [1,3,6,8,10,13,15,18,20,22]:
			keylist[i].image = pyglet.image.load("black.png")
	for i in turnlist:
		if i in [0,5,12,17]:
			keylist[i].image = pyglet.image.load("whiteAH.png")
		if i in [2,7,9,14,19,21]:
			keylist[i].image = pyglet.image.load("whiteBH.png")
		if i in [4,11,16,23]:
			keylist[i].image = pyglet.image.load("whiteCH.png")
		if i in [1,3,6,8,10,13,15,18,20,22]:
			keylist[i].image = pyglet.image.load("blackH.png")