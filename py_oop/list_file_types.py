#How to Create and Write to a File in Python
#Create and add content to a file 
#open() method opens the file if it exists or it will create it if it doesn't
#open is built into the Python language

#Creates object, file builder represents what the file is. 

file_builder = open("logger.txt", "w+")

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n") #\n allows you to add a carriage return

for i in range(1000):
    file_builder.write(f"I'm on line {i + 1}\n") #Runs file

file_builder.write("Hey, I'm in a file!")
#Calls function on the file 

file_builder.close() 

#ie. Compression : Use case
#Making files smaller so you can use them
#Looking for patterns you can chop down to a key
#ie. Writing a compression algorithm, for backend code or scrapping data
