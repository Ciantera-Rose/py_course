#Reading and Working with File Data in Python


#Create a function
#Take a file name as path in as argument
#Use open function and pass in filename argument, path to file, and 'r' to read the file

def get_file_contents(filename):
    queried_file = open(filename, 'r')

    if queried_file.mode == 'r': #Checks to see what type of mode file in. Read mode in this case
        return queried_file.read() #Calls read function


content = get_file_contents('file-section/text_content.txt') #Stored what got return. Gives access to the file you want to work with
#Calls read function, passes in path to the file.
#Wherever you call file from is consdered the root of the path

print(content)

print("Number of words", len(content.split())) #Split function turns words into list elements