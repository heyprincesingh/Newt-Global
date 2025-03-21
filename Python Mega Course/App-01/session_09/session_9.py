while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            todos = file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}", end="")

    elif "edit" in user_action:
        number = int(user_action[4:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ") + "\n"
        todos[number - 1] = new_todo

        with open("todos.txt", "w") as file:
            todos = file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.pop(number - 1)

        with open("todos.txt", "w") as file:
            todos = file.writelines(todos)

    elif "exit" in user_action:
        break
    else:
        print("Command not valid")

print("Bye!")
