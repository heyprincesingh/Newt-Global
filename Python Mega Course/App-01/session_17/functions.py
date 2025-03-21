DEFAULT_FILEPATH = "todos.txt"

def get_todos(filepath=DEFAULT_FILEPATH):
    """Read a text file and return the list of"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local
    
def write_todos(todos, filepath=DEFAULT_FILEPATH):
    """Write a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos)