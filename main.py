import functions
import time

now = time.strftime("%b, %d,%Y %H:%M:%S")
print(now)
while True:
    userAction = input("Type, add,show, complete, or exit: ")
    userAction.strip()

    if userAction.startswith("add"):
            todo = userAction[4:]

            todos = functions.getTodos()
            todos.append(todo+'\n')

            functions.writeTodos(todos)


    elif userAction.startswith("show"):
        todos = functions.getTodos()

        todos = [todo.strip("\n") for todo in todos]

        for index, todo in enumerate(todos):
            print(index+1,todo)

    elif userAction.startswith("edit"):
        try:
            indexToEdit = int(userAction[5:])-1
            newTodo = input("Enter new text: ")

            todos = functions.getTodos()

            todos[indexToEdit] = newTodo+"\n"

            functions.writeTodos(todos)
        except ValueError:
            print("Your comand is not valid")

    elif userAction.startswith("complete"):
        try:
            indexToDelete = int(userAction[9:])
            indexToDelete = indexToDelete -1

            todos = functions.getTodos()
            todoToDelete = todos[indexToDelete]
            todos.pop(indexToDelete)

            functions.writeTodos(todos)

            print(todoToDelete.strip("\n") + " has been deleted")

        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("Todo does not exist")
    elif userAction == "exit":
        break
    else:
        print("Enter a recognized command")