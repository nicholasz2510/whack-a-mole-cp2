t = False

def setup():
    fullScreen()
    frameRate(90)

def draw():
    global t
    background(255)
    menuMockup = loadImage("../../Assets/MainMenuMockup.png")
    tableMockup = loadImage("../../Assets/tableMockup.png")
    if t:
        image(tableMockup, 0, 0, displayWidth, displayHeight)
    else:
        image(menuMockup, 0, 0, displayWidth, displayHeight)
        
    
def mouseClicked():
    global t
    t = not t
