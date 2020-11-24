#How to Build a Custom Iterator Class in Python
#By creating our own custom iterator it gives us complete control of how we iterate through the collection

class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1) 
#Subtract 1 b/c we don't want the length, just the value of the last index. Need it to not have off by one errors
#Running a query in the list
    def __iter__(self):
        self.n = 0
        return self

#Dunder iter needs to return self
#Set to 0 so we can keep track of where we are in the lineup      

    def get_player(self, n):
        return self.players[n]

#Will allow us to call next on the items
#Runs the condition
    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player

#We instantiated our class and made our list 
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

astros_lineup = Lineup(astros)
#Cretae a process and call iter function on astros lineup
#Dunder method goes step by step of what will happen throughout this process
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
