import operator
from functools import reduce

#CODING CHALLENGE

#Build out a function called dynamic reducer, it takes in a list and a operator as a string and then it should perform computation on that list
#Research Python libraries 
#Pass in fucntion and have that function run over the entire collection

"""
dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '+') # -
dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '+') # 6
"""

#Dynamic reducer is going to take in a collection and an operator as the arguments
#Create a dictionary
#Use operator library to call the function

def dynamic_reducer(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.subtract,
        "*": operator.mul,
        "/": operator.truediv
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 3], '+')) 
print(dynamic_reducer([1, 2, 3], '-')) 
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))


#A dictionary named operators with a set of key value pairs. Each one of the keys is a string and the value is a function.
#When you call the string in the key, this will return the function of the operator in the value when you pass it in.
#We perform a lookup with the operators and use the reduce library.
#The first argument you pass in is a function, the lamba function. The lamba has a total and an element: 
#The operators (our dictionary name), we pass in the key [op] which references the second argument we passed in to the function.
#When we preform this lookup a function gets sent back to us, meaning it can be called directly and then pass in what it expects.
#The value operators all expect two arguments. The total and the element.
#Reduce allows us to pass in a function and that function can perform any number of processes we need it to. Used for simple processes. 
#The operator functions are being called directly, reduce keeps track of a total and iterates over each of the elements in the collection, making it dynamic.
