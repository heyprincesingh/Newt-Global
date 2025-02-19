while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}", end="")

        case "edit":
            number = int(input("Enter a todo number to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()
                
            todos[number] = new_todo

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)
                
        case "complete":
            number = int(input("Enter a todo number to complete: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            todos.pop(number - 1)

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        case "exit":
            break

print("Bye!")
