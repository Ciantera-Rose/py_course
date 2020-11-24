#Overview of Dunder Methods in Python: __init__
#Two underscores followed by inti and then two more underscores
#This speaks to the way Python uses private and public methods of data that communicates how the data should be used
#Private/protected: Gives a visual cue as to not use data outside of their classes 
#Dunder methods mean it is a method given to you by Python language directly to define the same way and not override the reserve word

#Dunder string __str__
#Python looks for the method in a class and can give you helpful information about what's in that class
#The ability to dump out all of the values specific to an object

class Invoice:
  def __str__(self):
    return "This is the invoice class!"


inv = Invoice()
print(str(inv))

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"


inv = Invoice('Google', 500)
print(str(inv))