# Function to Process a List 2
# The get_max function you created in the previous exercise returned 9.7. 

# In this exercise, you should:
# (1) change the function so this time it returns the following string:
# "Max: 9.7, Min: 9.2"
# where 9.7 is the maximum, and 9.2 is the minimum.
# Note: For the exercise to be marked as correct by the system, you should return the exact string "Max: 9.7, Min: 9.2"

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return f"Max: {maximum}, Min: {minimum}"
    
print(get_max())