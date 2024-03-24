import PySimpleGUI as psg
import functions

inputLabel = psg.Text("Enter A Todo")
todoInputBox = psg.InputText("",key="todoInputBox", tooltip="Enter a Todo")

addTodoButton = psg.Button("Add", key="addTodoButton")

editTodoButton = psg.Button("Edit",key="editTodoButton")

completeTodoButton = psg.Button("Complete", key="completeTodoButton")

exitButton = psg.Button("Exit", key="exitButton")

todosList = psg.Listbox(size=(45,10), values=functions.getTodos(),
                        key="todosList", enable_events=True)

window = psg.Window("Todo App",
                    layout=
                    [[inputLabel],
                     [todoInputBox],
                     [todosList,addTodoButton,editTodoButton, completeTodoButton],
                     [exitButton]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "addTodoButton":
            todos = functions.getTodos()

            newTodo = values["todoInputBox"] + "\n"
            todos.append(newTodo)

            functions.writeTodos(todos)

            window["todosList"].update(values=todos)
            window["todoInputBox"].update(value=" ")

        case "editTodoButton":
            try:
                todoToEdit = values["todosList"][0]
                newTodoText = values["todoInputBox"]

                todos = functions.getTodos()
                todoToEditIndex = todos.index(todoToEdit)

                todos[todoToEditIndex] = newTodoText + '\n'

                functions.writeTodos(todos)

                window["todosList"].update(values=todos)
            except IndexError:
                psg.popup("Please select a Todo First")

        case "completeTodoButton":
            try:
                todoToComplete = values["todosList"][0]

                todos = functions.getTodos()
                todoToCompleteIndex = todos.index(todoToComplete)

                todos.pop(todoToCompleteIndex)

                functions.writeTodos(todos)

                window["todosList"].update(values=todos)
                window["todoInputBox"].update(value=" ")
            except IndexError:
                psg.popup("Please select a Todo First")
        case "exitButton":
            break

        case psg.WINDOW_CLOSED:
            break

window.close()
