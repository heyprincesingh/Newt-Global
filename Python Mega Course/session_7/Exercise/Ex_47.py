# Sum of Numbers
# Extend the given code so it prints out the sum of the numbers. Note that the numbers are currently string types.

# The output of your code should be as below:

# 49.1

user_entries = ['10', '19.1', '20']

user_entries = [float(entry) for entry in user_entries]
print(sum(user_entries))