# With Context Manager -File Writing
# The code in the coding area creates a new file.txt file and writes the text snail inside the file. 
# Your task is to rewrite the code by using a with-context manager.

# file = open('file.txt', 'w')
# file.write('snail')
# file.close()

with open('file.txt', 'w') as file:
    file.write('snail')