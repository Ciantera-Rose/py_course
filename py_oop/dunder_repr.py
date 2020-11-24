#Overview of Dunder Methods in Python: __repr__

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"
#Taking a look as a custom view to see what data is inside   

  def __repr__(self):
    return f"Invoice({self.client}, {self.total})"
#True raw data of the instance of the class


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))