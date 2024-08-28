## in this file i will be using OOP techniques to make the logic for the rummykub game

## there are 106 tiles in the standard game
## 12 sets of tile 1-13 in black, red, blue, yellow
## 4 jokers

import random

COLOURS = ['BLACK', 'RED', 'BLUE', 'YELLOW']
MAX_NUMBER = 14

class tile:
    def __init__(self, value, colour):
        ## how would i represent the joker
        self.value = value
        self.colour = colour

    def to_string(self):
        return f"{self.value}{self.colour}"
    
class bag:
    def __init__(self):
        # add the starting tiles to the bag
        self.bag = []

        for _ in range(2):
            for colour in COLOURS:
                for value in range(1, MAX_NUMBER):
                    self.bag.append(tile(value, colour))

        for _ in range(2):
            self.bag.append(tile('JOKER', ''))

    def choose(self):
        # returns a randomly chosen tile and deletes it from the bag
        choice = random.choice(self.bag)
        self.bag.remove(choice)
        return choice
       
class player:
    bag = bag()
    def __init__(self):
        self.rack = []

    def pick_up(self):
        #chose a random tile from the bag
        self.rack.append(self.bag.choose())

    def to_string(self):
        string = ""
        for tile in self.rack:
            string += tile.to_string() 
        
        return string

## what do I think I should do here
## have a board class
## the board class then contains many sets - groups or runs (could use inheritance for this)
## yeah i think this makes the most sense

class set:
    def __init__(self):
        ## not sure what should be going in here 
        ## what would be the utilty 

        # could just create the list to store the tiles
        # and add the tiles to the list (allowing a variable ammount of tiles to be added the tiles list)
        # though I have concerns that all of the logic apart from having more than 3 tiles is specific to the type of set
        
        pass

class run:
    def __init__(self, *tiles):
        # i only want a run to be created if the conditions are met
        self.contents = []

        for tile in tiles:
            self.contents.append(tile)

    def check(self):
        ## would need to check that all tiles are of the same colour
        ## then check that all of the values are sequential

        ## do each of these things ignoring jokers
        pass

class group:
    def __init__(self, *tiles):
        # i only want a run to be created if the conditions are met
        self.contents = []

        for tile in tiles:
            self.contents.append(tile)

    def check(self):
        ## would need to check that all tiles are of the same colour
        ## then check that all of the values are sequential

        ## do each of these things ignoring jokers
        pass

player1 = player()
player2 = player()

## this works as hoped :)

 

