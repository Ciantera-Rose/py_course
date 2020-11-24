#Guide to Python's __init__ Constructor Function

git#Notes

#Classes are made up of data and behavior
#Contructor Function: Use dunder __inti__ method
#This function will be called whenever you instantiate the class
#It will add the data into the class
#Remeber every method inside of a class needs self passed into it as an argument
#Everything in Python is an object. So we are creating variables that are directly related to the instance

class Invoice:
    def __init__(self, client, total):
        #Self binds them as properities of that object
        #aka assigned arguements to the object
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'

google = Invoice('Google', 100) 
snapchat = Invoice('SnapChat', 200) 

print(google.formatter())
print(snapchat.formatter())
