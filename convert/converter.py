class Converter():
    
    def __init__(self):
        self.multiplier=1.61
    
    def to_usd(self, value):
        return value * self.multiplier
