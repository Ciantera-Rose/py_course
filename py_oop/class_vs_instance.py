#Class vs Instance Attributes in Python
#An instance belongs to an instance and must be called on an instance of that class
#A class attirbute belongs to the class, a hard coded value that belongs to that class.
#A class attribute belongs to a classs definition

class Website:
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title') #Instantiation of an attribute in the class
print(ws.__dict__)

ws_two = Website('My Second Title') #Another instance attribute with a new argument
print(ws_two.__dict__) #Dunder dict is casting a dict view


class DifferentWebsite: #Class attribute with a hard coded value
  title = 'My Class Title'

dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)