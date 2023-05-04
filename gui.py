import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")
clock_label = sg.Text('', key='clock')
label = sg.Text("Type in a To-D0")
input_box = sg.InputText(tooltip="Enter To-Do",
                         key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit", size=5)
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[35, 10])
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('MY To_Do App', layout = [[clock_label],[label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]     ],
                   font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.add_todos(todos)
                window['todos'].update(values=todos)

        case 'Edit':
            try:
                todos_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todos_to_edit)
                todos[index] =new_todo
                functions.add_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select an item First To Edit", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.add_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please First Select Item to Complete", font=("Helvetica", 14))

        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            exit()

window.close()
