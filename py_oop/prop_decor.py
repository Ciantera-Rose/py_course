#How to Work with Python Properties and Decorators
#Property decorator fits the issue where everyone has access to all of the data
#We may want to protect some element so it doesn't get overwritten
#Standard convention: Anytime you are dealing with data you want it to be private or protected
#Protected means child classes will have access to that data. represented by an underscore in front of data
#Private attribute will use two underscores meaning it shouldn't chnaged in other places throughout the document
#These are indications about how we want to use the data
#Syntactic sugar that takes in a function and passes a an argument


class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'
        print(goole.property)

    @property
    def client(self):
        return self._client
#Used property decorator to directly call on client
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
