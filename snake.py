import random
from tkinter import *
from PIL import Image, ImageTk

WIDTH = 1000
HEIGHT = 650
BODYSIZE = 50
STARTDELAY = 500
LENGTH = 3

countBodyW = WIDTH / BODYSIZE
countBodyH = HEIGHT / BODYSIZE
x = [0] * int(countBodyW)
y = [0] * int(countBodyH)
print(x)
print(y)


class Snake(Canvas):

    headImage = False
    head = False
    body = False
    apple = False
    delay = 0
    direction = "Right"
    loss = False

    def __init__(self):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT,background="black")
        self.focus_get()
        self.bind_all("<Key>", self.onKeyPressed)
        self.loadResourses()
        self.beginPlay()
        self.pack()


    def loadResourses(self):
        self.headImage = Image.open("images/head.png")

        self.head = ImageTk.PhotoImage(self.headImage.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.body = ImageTk.PhotoImage(Image.open("images/body.png").resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.apple = ImageTk.PhotoImage(Image.open("images/apple.png").resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))

    def beginPlay(self):
        self.delay = STARTDELAY
        self.direction = "Right"
        self.loss = False

        self.delete(ALL)
        self.spawnActors()
        self.after(self.delay, self.timer)

    def spawnActors(self):

        self.spawnApple()

        global x
        global y
        x[0] = int(countBodyW / 2) * BODYSIZE
        y[0] = int(countBodyH / 2) * BODYSIZE
        for i in range(1, LENGTH):
            x[i] = x[0] - BODYSIZE * i
            y[i] = y[0]
        
        self.create_image(x[0], y[0], image=self.head, anchor="nw", tag="head")
        
        for i in range(1, LENGTH):
             self.create_image(x[i], y[i], image=self.body, anchor="nw", tag="body")


    def spawnApple(self):
        apple = self.find_withtag("apple")
        if apple:
            self.delete(apple[0])
        rx = random.randint(0, countBodyW - 1)
        ry = random.randint(0, countBodyH - 1)
        self.create_image(rx * BODYSIZE, ry * BODYSIZE, anchor="nw", image=self.apple, tag="apple")

    def onKeyPressed(self, event):
        key = event.keysym
        print(key)
        


    def updateDirection(self):
        pass



    def timer(self):
        if not self.loss:
            self.moveSnake()
            self.updateDirection()
            self.after(self.delay, self.timer)


    def moveSnake(self):
        head = self.find_withtag("head")
        body = self.find_withtag("body")
        item = body + head
        for i in range(len(item) - 1):
            currentxy = self.coords(item[i])
            nextxy =self.coords(item[i+1])
            self.move(item[i], nextxy[0] - currentxy[0], nextxy[1] - currentxy[1])

        if self.direction == "Left":
            self.move(head, -BODYSIZE, 0)
        elif self.direction == "Right":
            self.move(head, BODYSIZE, 0)
        elif self.direction == "Up":
            self.move(head, 0, -BODYSIZE)
        elif self.direction == "Down":
            self.move(head, 0, BODYSIZE)


root = Tk()
root.title("My Snake")
root.board = Snake() 

root.resizable(False, False)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = int(ws / 2 - WIDTH / 2)
y = int(hs / 2 - HEIGHT / 2)

root.geometry("+{0}+{1}".format(x, y))

root.mainloop()
