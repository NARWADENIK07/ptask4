Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors 

try:
    file1 = open('sample.txt','r')      # Tries to open 'sample.txt' in read mode
    read = file1.read()                 # Reads the entire content of the file
    print(read)                         # Prints the file content
    file1.close()                       # Closes the file after reading
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")  # If file is missing, shows an error

finally:
    print()  # Always runs — in this case, just prints a blank line


Task 2: Write and Append Data to a File

Takes user input and writes it to a file (output.txt), replacing any existing content.

Takes more input and appends it to the same file.

Reads and displays the final content of the file.

It demonstrates writing, appending, and reading from a file using user input.
