import pyglet
import keys
from pyglet.window import mouse


window = pyglet.window.Window(1280, 720, resizable = False)

keyList = keys.getKeys()

@window.event
def  on_draw():
	for key in keyList:
		key.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT and 181<=x<=241 and 210<=y<=510:
		keys.turn(keyList,[0])

pyglet.app.run()