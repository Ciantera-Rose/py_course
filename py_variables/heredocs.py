#Multi-line strings in programming typically are called `Heredocs`
#Heredoc
#Can be either single or double quotes
#Heredocs are multi-line strings that count all of the newline characters

# Heredoc

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()

print(content)

#.strip() funciton at the very end of the string will remove the new line characters from the beginning and the end of the string
