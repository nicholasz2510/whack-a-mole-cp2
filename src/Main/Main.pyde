from Hole import Hole

h = Hole(3, (5, 3), "test")
h.generate()
print(h.m.speed)
h.destroy()

def setup():
    fullScreen()
    frameRate(90)

def draw():
