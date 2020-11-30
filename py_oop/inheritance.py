#Introduction to Inheritance in Python
#At a high level inheritance is the ability to create specialized versions of classes.
#It allows us to define a class that inherits all the methods and properties from another class. 


class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self):  #Fucn globally available to all users
    return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User): #This class attribute inherits from user and we create a custom function witin that class
  def active_users(self):
    return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

#SO the AdminUser class inherits all the function of the User class with new specialized functions specific to only the Admin class

print(tiffany.active_users())
print(tiffany.greeting())
print(kristine.active_users())