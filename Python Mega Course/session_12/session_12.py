def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local
    
def write_todos(filepath, todos):
    with open(filepath, "w") as file:
        file.writelines(todos)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos(filepath="todos.txt")

        todos.append(todo)
        
        write_todos(filepath="todos.txt", todos=todos)

    elif user_action.startswith("show"):
        todos = get_todos(filepath="todos.txt")

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}", end="")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:])

            todos = get_todos(filepath="todos.txt")

            new_todo = input("Enter a new todo: ") + "\n"
            todos[number - 1] = new_todo

            write_todos(filepath="todos.txt", todos=todos)

        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos(filepath="todos.txt")

            todos.pop(number - 1)

            write_todos(filepath="todos.txt", todos=todos)

        except ValueError or IndexError:
            print("Command not valid")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid")

print("Bye!")
