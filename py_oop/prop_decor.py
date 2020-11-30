#How to Work with Python Properties and Decorators
#Property decorator fits the issue where everyone has access to all of the data
#We may want to protect some element so it doesn't get overwritten
#Standard convention: Anytime you are dealing with data you want it to be private or protected
#Protected means child classes will have access to that data. represented by an underscore in front of data
#Private attribute will use two underscores meaning it shouldn't chnaged in other places throughout the document
#These are indications about how we want to use the data
#Syntactic sugar that takes in a function and passes a an argument
#Gives a clear distinction in your of how you want to call on your objects

class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'
        print(google.formatter)
        print(goole.property)

    @property
    def client(self):
        return self._client
#Used property decorator to directly call on client (property) that we want to work with
# _ communites that these objects should only be called within this class

    @client.setter
    def client(self, client):
        self._client = client
#Taking the data and setting to something else   
#Takes in a function passes in an argument and sets it to a new value

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)
print(google.client)

print(google.client)
print(google.total)

google.client = 'Yahoo'

print(google.client)

'''
A decorator is any callable object that is used to modify a function or a class.
A reference to a function "func" or a class "C" is passed to a decorator and the 
decorator returns a modified function or class. Syntactic sugar that takes in a 
function and passes an argument, gives a clear distinction in your code of how you 
want to call on and work with your objects. Whubbaa dub!

'''
