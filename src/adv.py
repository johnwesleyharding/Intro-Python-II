
from room import Room
from player import Player
from item import Item

# Declare items before rooms

cloak = Item('cloak', 'The cloak itself is invisible.')
shield = Item('shield', 'It will keep the rain off of your head.')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                    [cloak]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    [shield]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
hero = Player('Hero')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# turn_limit = 1000000
# for i in range(turn_limit):

print(room[hero.room].name)
print(room[hero.room].description)

while True:
    
    print()
    action = input('Action? ').lower().split(' ')
    
    if len(action) > 1:
        
        target = action[1]
        
    action = action[0]
    
    if action in ('n', 'e', 's', 'w'):
        
        action += '_to'
        
        if getattr(room[hero.room], action) == None:
            
            print('cannot advance in this direction')
            
        else:
            
            hero.room = getattr(room[hero.room], action)
            print(room[hero.room].name)
            print(room[hero.room].description)
            
            if room[hero.room].items != None:
                
                print(f'The room contains: {[x.name for x in room[hero.room].items]}')
#                 print(f'The room contains:')
                
#                 for item in room[hero.room].items:
                    
#                     print(item.name)
    
    elif action in ('i', 'inventory'):
        
        if len(hero.items) > 0:
            
            print('You hold these items:')
            for item in hero.items:
                
                print(item.name)
                            
        else:
            
            print('You have no items.')
        
    
    elif action in ('take', 'get'):
        
        stuff = []
        for item in room[hero.room].items:
                
            stuff.append(item.name)
        
        if target in stuff:

            hero.items.append(target)
#             room[hero.room].items.remove(target)
            print(room[hero.room].items)
            print(f'You take the {target.name}.')
            print(target.description)
            
        else:
            
            print('There is no such item here.')
            print(room[hero.room].items)
            
    elif action == 'drop':
        
        if target in hero.items:
            
            hero.items.remove(target)
            print(f'You drop the {target.name}; it hits the floor and shatters.')
            
        else:
            
            print('You possess no such item.')
        
    elif action == 'q':
        
        break
        
    else:
        
        print('Enter n, e, s, w to move, q to quit, i to see inventory, take <item>, or drop <item>')
