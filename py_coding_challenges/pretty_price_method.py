from helper import data

#Build a Pretty Price Method in Python

#Have a function so that when it's called, if it's passed in a gross vaule, like sale price, the ouput of the function should be formatted
#pretty_price(3.20, 99) should output 3.99
#More flexible so if you pass in a decimal, output would be the same.
#Goal is to have both working

#Build a price formatter
# x = 3.50
#Strip away, convert to integer
#int(x)
#Need to check if extention is a decimal or an interger

def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension

print(pretty_price(3.50, 0.95))
print(pretty_price(3.50, 95))
