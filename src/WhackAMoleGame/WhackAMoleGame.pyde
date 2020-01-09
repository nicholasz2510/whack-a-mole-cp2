class Game:
    
    
    
    def __init__(self):
        self.points = 0
        self.moleSpawnTimer = Timer()
        self.emptyHoleArray = []
        self.fullHoleArray = []
    
    def setup():
        size(1920, 1080)
        frameRate(90)
                
    def gameStart(self):
        print "game started"
        
    def gameEnd(self):
        print "game ended"
    
    def draw():
        background(255)
    draw()
