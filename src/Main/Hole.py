from Mole import Mole
class Hole:
    
    
    def __init__(self, moleDeletionTimer, coords, name):
        self.moleDT = moleDeletionTimer
        self.coords = coords
        self.name = name
        self.hitboxBool = False
        self.m = None
        
        
    def generate(self):
        self.m = Mole((5, 3), 1, 1)
        
    def destroy(self):
        del self.m
        self.m = None
