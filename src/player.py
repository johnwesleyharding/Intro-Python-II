# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__(self, name, room = 'outside'):
        
        self.name = name
        self.room = room
        self.items = []
