class Game:
    
    
    
    def __init__(self):
        self.points = 0
        self.moleSpawnTimer = Timer()
        self.emptyHoleArray = []
        self.fullHoleArray = []
    
    def setup():
        size(int(displayWidth / 20) * 20, (int(displayHeight / 20) * 20) - 40)
        frameRate(100)
                
    def gameStart(self):
        None
        
    def gameEnd(self):
        None
