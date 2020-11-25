#Appending to a File in Python

import datetime
from time import sleep

for i in range(5):
    file_builder = open("logger.txt", "a+")
    file_builder.write(f'{datetime.datetime.now()}\n')
    file_builder.close()

    print("file created")

    sleep(1)

#Imported sleeptime library
#Created range 1-5
#Created a file object
#Created a+ option flag to append file
#File gets created at the root of the application. 
#At the root of the repositiory
#You may pass in a path if you choose
#We created a logger file with 5 entires    
#The script appends to the current file and does not override them