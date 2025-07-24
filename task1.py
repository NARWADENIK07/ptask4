
try:
    file1 = open('sample.txt','r')
    read = file1.read()
    print(read)
    file1.close()
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
finally:
    print()




