def get_todos():
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            todos = file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}", end="")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:])

            todos = get_todos()

            new_todo = input("Enter a new todo: ") + "\n"
            todos[number - 1] = new_todo

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todos.pop(number - 1)

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        except ValueError or IndexError:
            print("Command not valid")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid")

print("Bye!")
