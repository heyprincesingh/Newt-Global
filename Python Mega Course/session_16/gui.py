import FreeSimpleGUI as sg  # type: ignore

layout = [
    [sg.Text("Type in a to-do")],
    [
        sg.InputText(tooltip="Enter todo"),
        sg.Button("Add"),
    ],
]

window = sg.Window("Todo App", layout=layout)
window.read()
window.close()
