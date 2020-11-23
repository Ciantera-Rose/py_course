#Overview of Python's strip, lstrip, and rstrip Functions
#Strip() function clears thhe whtie space at the beginning and end of the string
#You may also pass in the portion of the sring you want to strip

url = 'https://google.com'

print(url.strip('https://'))
#returns google.com

#Return Google

#lstrip() and rstrip() to strip each side you pass in leaving just the portion you want.
url = url.lstrip('https://')
url = url.rstrip('.com')

#capitalize just the first letter
print(url.capitalize())

#Google