import FreeSimpleGUI as sg  # type: ignore
from functions import get_todos, write_todos

layout = [
    [sg.Text("Type in a to-do")],
    [
        sg.InputText(tooltip="Enter todo", key="todo"),
        sg.Button("Add"),
    ],
    [sg.Listbox(values=get_todos(), key="todos", enable_events=True, size=[45, 10]), sg.Button("Edit"), sg.Button("Complete")],
]

window = sg.Window(
                "Todo App",
                layout=layout,
                font=("Helvetica", 20),
            )

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = get_todos()
            todo = values["todo"] + "\n"
            todos.append(todo)
            write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 18))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 18))

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break


window.close()
