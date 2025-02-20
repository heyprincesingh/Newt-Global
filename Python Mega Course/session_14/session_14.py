import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos(filepath="todos.txt")

        todos.append(todo)
        
        functions.write_todos(filepath="todos.txt", todos=todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos(filepath="todos.txt")

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}", end="")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:])

            todos = functions.get_todos(filepath="todos.txt")

            new_todo = input("Enter a new todo: ") + "\n"
            todos[number - 1] = new_todo

            functions.write_todos(filepath="todos.txt", todos=todos)

        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos(filepath="todos.txt")

            todos.pop(number - 1)

            functions.write_todos(filepath="todos.txt", todos=todos)

        except ValueError or IndexError:
            print("Command not valid")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid")

print("Bye!")
