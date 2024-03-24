FILEPATH = 'todos.txt'

def getTodos(filepath=FILEPATH):
    """Extracts the values new line separated strings in the todos.txt file into a list"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def writeTodos(content,filepath=FILEPATH):
    """Write the todos list into the todos.txt file"""
    with open(filepath, 'w') as file:
        file.writelines(content)


if __name__ == '__main__':
    print("functions is main")