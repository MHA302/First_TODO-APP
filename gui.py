import functions
import PySimpleGUI as sg



label = sg.Text("Type in a To-D0")
input_box = sg.InputText(tooltip="Enter To-Do",
                         key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])

window = sg.Window('MY To_Do App', layout = [[label],
                             [input_box, add_button],
                             [list_box, edit_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.add_todos(todos)
                window['todos'].update(values=todos)

        case 'Edit':
            todos_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todos_to_edit)
            todos[index] =new_todo
            functions.add_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break


window.close()
