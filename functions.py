PATHFILE='todo.txt'


#def readfile(pathfile="/Users/gmashaka/PycharmProjects/todos/files/todo1.txt"):
def readfile(pathfile=PATHFILE):
    """
    read a file and return the content
    :param pathfile:
    :return: todo list
    """
    with open(pathfile, "r") as file:
        content1 = file.readlines()
        return content1

def writefile(todos, pathfile=PATHFILE):
    """
    write a file
    :param todos:
    :param pathfile:
    :return: nothing
    """
    with open(pathfile, "r+") as file:
        file.writelines(todos)

if __name__ == "__main__":
    print(readfile())
    print("Hello World")