# With Context Manager -Analyzing Content
# The code in the coding area successfully reads and prints out the number of characters in the bear.txt file. 
# Similar to the previous task, your task is to rewrite the code by using a "with" context manager to achieve the same thing.

# file = open("essay.txt", 'r')
# content = file.read()
# file.close()

# nr_chars = len(content)
# print(nr_chars)

with open("essay.txt", 'r') as file:
    content = file.read()

nr_chars = len(content)
print(nr_chars)