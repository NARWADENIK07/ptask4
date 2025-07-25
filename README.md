Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors 

try:
    file1 = open('sample.txt','r')
    read = file1.read()
    print(read)
    file1.close()
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
finally:
    print()

Task 2: Write and Append Data to a File
