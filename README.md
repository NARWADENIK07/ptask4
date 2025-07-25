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

text_write = input('Enter text to the file: ')
with open('output.txt','w') as file:
    file.write(text_write + "\n")

print('Data successfully written to output.txt.')

text_append = input('Enter additional text to append: ')
with open('output.txt','a') as file:
    file.write(text_append + '\n')

print('Data successfully append')

print('\nFinal content of output.txt:')
with open('output.txt','r') as file:
    content = file.read()

print(content) 
