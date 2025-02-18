user_prompt = input("Enter a todo item: ")

todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)