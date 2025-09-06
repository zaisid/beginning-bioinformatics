
import os

def get_filename(test=False): #get filename from directory
    '''Returns file name of a .txt file in current directory'''
    for file_name in os.listdir(): 
        if ".txt" in file_name: #search specifically for .txt files
            if test == True:
                return("test.txt")
            if file_name == "test.txt":
                continue
            return(file_name) 

def text_from_file(test=False):
    '''Returns text of file path given by get_filename()'''
    with open(f"{os.getcwd()}/{get_filename(test)}") as f: 
        text = f.read() #get text from file
    return text

def str_to_int(numbers):
    '''Converts all elements of list into integers & returns list'''
    for ind,num in enumerate(numbers):
        integer = int(num)
        numbers[ind]=integer
    return numbers
        
