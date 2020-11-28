#How to Get and Set Data in a Python Class
#Essentially realize that you can overide and set the values as something different. 
#Be careful to pay attention as it may lead to a lot of debugging

class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo' 
#We can set values after we have created the entire object.
#A setter process that allows us to override the original value
#So we can use getters and setters without having to create the functions inside of python 

print(google.client)
print(google.total)

