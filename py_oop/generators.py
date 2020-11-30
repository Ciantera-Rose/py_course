#Overview of Iterators vs Generators in Python
#A generator allows you to yield an iteration to a particiluar method until you call it again
#It is a simple way of creating iterators. It is a function that returns an object (iterator) which we can iterate over (one value at a time). 


class InfiniteLineup:
    def __init__(self, players): #Starts w/ an init method
        self.players = players #Lets us bring in players list

    def lineup(self):
        lineup_max = len(self.players) #Brings in total count of players that are there
        idx = 0 #Sets index to 0      

#Creates inifinte loop

        while True:
            if idx < lineup_max:
                yield self.players[idx] #Generators use yield keyword. Yields to generator. Python creates a generator object
            else:
                idx = 0 #Resets index
                yield self.players[idx]

            idx += 1 #While inside loop and increment index by 1

    def __repr__(self):
        return f'InfiniteLineup({self.players})'
#Repr functions takes in self and returns entire object

    def __str__(self):
        return f"InfiniteLineup with the players: {', '.join(self.players)}"
#Dunder string method: We pass in list of players in the argument

astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

full_lineup = InfiniteLineup(astros) #This instantiates our list of platers
astros_lineup = full_lineup.lineup() #Needs to call lineup method

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))

print(str(full_lineup))