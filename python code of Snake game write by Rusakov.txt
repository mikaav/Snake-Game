from tkinter import *


class Snake(Canvas):

    def __init__(self):
        pass


root = Tk()
root.title("Snake")
root.board = Snake()

root.resizable(False, False)
w = root.winfo_reqwidth()
h = root.winfo_reqheight()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)

root.geometry("+{0}+{1}".format(x, y))

root.mainloop()
