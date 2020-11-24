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

print(google.client)
print(google.total)

