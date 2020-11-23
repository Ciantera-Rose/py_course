#String Interpolation
#Allows you to process/run python code inside of strings
#You can implement str int using the format flag f' {...}' syntax.
#If you ever want the brackets to appear in the text simply use double brackets {{...}}

#ie. Use Str Int in a Heredoc to dynamically type and email

name = 'Kristine'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content)