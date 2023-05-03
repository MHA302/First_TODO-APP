FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reading text file
    and return the list from  to_do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def add_todos(todos_arg, filepath=FILEPATH):
    """ writing text file
        and return the list from  to_do items
        """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from the functions")
    print(get_todos())
