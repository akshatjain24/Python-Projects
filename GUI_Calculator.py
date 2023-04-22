from tkinter import *

def click(event):
    global screen_value
    text = event.widget.cget("text")
    if text == "=":
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            value = eval(screen.get())
        screen_value.set(value)
        screen.update()
    elif text == "AC":
        screen_value.set("")
        screen.update()
    elif text == "^":
        screen_value.set(screen_value.get() + "**")
        screen.update()
    elif text == "÷":
        screen_value.set(screen_value.get() + "/")
        screen.update()
    elif text == "X":
        screen_value.set(screen_value.get() + "*")
        screen.update()
    elif text == "DEL":
        screen_value.set(screen_value.get()[0:len(screen_value.get())-1])
        screen.update()
    elif text == "%":
        screen_value.set(screen_value.get() + "/100*")
        screen.update()
    else:
        screen_value.set(screen_value.get() + text)
        screen.update()

root = Tk()
root.geometry("305x285")
root.minsize(305,285)
root.maxsize(305,285)
root.title("Calculator ~ Akshat Jain")

screen_value = StringVar()
screen_value.set("")

screen = Entry(root, textvar = screen_value, font="comicsansms 14 ")
screen.pack(fill=X,ipady = 5, padx = 10, pady = 10)


frame = Frame(root, bg="grey")

b7 = Button(frame, text="7", font="comicsnsms 18", padx = 8)
b7.pack(side = LEFT, padx = 4, pady = 4)
b7.bind("<Button-1>", click)
b8 = Button(frame, text="8", font="comicsnsms 18", padx = 8)
b8.pack(side = LEFT, padx = 4, pady = 4)
b8.bind("<Button-1>", click)
b9 = Button(frame, text="9", font="comicsnsms 18", padx = 8)
b9.pack(side = LEFT, padx = 4, pady = 4)
b9.bind("<Button-1>", click)
bD = Button(frame, text="DEL", font="comicsnsms 15", padx = 0, pady = 4)
bD.pack(side = LEFT, padx = 4, pady = 4)
bD.bind("<Button-1>", click)
bAC = Button(frame, text="AC", font="comicsnsms 16", padx = 2, pady = 3)
bAC.pack(side = LEFT, padx = 4, pady = 4)
bAC.bind("<Button-1>", click)
frame.pack()

frame = Frame(root, bg="grey")
b4 = Button(frame, text="4", font="comicsnsms 18", padx = 8)
b4.pack(side = LEFT, padx = 4, pady = 4)
b4.bind("<Button-1>", click)
b5 = Button(frame, text="5", font="comicsnsms 18", padx = 8)
b5.pack(side = LEFT, padx = 4, pady = 4)
b5.bind("<Button-1>", click)
b6 = Button(frame, text="6", font="comicsnsms 18", padx = 8)
b6.pack(side = LEFT, padx = 4, pady = 4)
b6.bind("<Button-1>", click)
bX = Button(frame, text="X", font="comicsnsms 15", padx = 12, pady = 4)
bX.pack(side = LEFT, padx = 4, pady = 4)
bX.bind("<Button-1>", click)
bdiv = Button(frame, text="÷", font="comicsnsms 16", padx = 10, pady = 3)
bdiv.pack(side = LEFT, padx = 4, pady = 4)
bdiv.bind("<Button-1>", click)
frame.pack()

frame = Frame(root, bg="grey")
b1 = Button(frame, text="1", font="comicsnsms 18", padx = 8)
b1.pack(side = LEFT, padx = 4, pady = 4)
b1.bind("<Button-1>", click)
b2 = Button(frame, text="2", font="comicsnsms 18", padx = 8)
b2.pack(side = LEFT, padx = 4, pady = 4)
b2.bind("<Button-1>", click)
b3 = Button(frame, text="3", font="comicsnsms 18", padx = 8)
b3.pack(side = LEFT, padx = 4, pady = 4)
b3.bind("<Button-1>", click)
bplus = Button(frame, text="+", font="comicsnsms 15", padx = 12, pady = 4)
bplus.pack(side = LEFT, padx = 4, pady = 4)
bplus.bind("<Button-1>", click)
bsub = Button(frame, text="-", font="comicsnsms 16", padx = 13, pady = 3)
bsub.pack(side = LEFT, padx = 4, pady = 4)
bsub.bind("<Button-1>", click)
frame.pack()

frame = Frame(root, bg="grey")
bdot = Button(frame, text=".", font="comicsnsms 18", padx = 11)
bdot.pack(side = LEFT, padx = 4, pady = 4)
bdot.bind("<Button-1>", click)
b0 = Button(frame, text="0", font="comicsnsms 18", padx = 8)
b0.pack(side = LEFT, padx = 4, pady = 4)
b0.bind("<Button-1>", click)
beq = Button(frame, text="=", font="comicsnsms 18", padx = 8)
beq.pack(side = LEFT, padx = 4, pady = 4)
beq.bind("<Button-1>", click)
bper = Button(frame, text="%", font="comicsnsms 15", padx = 9, pady = 4)
bper.pack(side = LEFT, padx = 4, pady = 4)
bper.bind("<Button-1>", click)
bpow = Button(frame, text="^", font="comicsnsms 16", padx = 12, pady = 3)
bpow.pack(side = LEFT, padx = 4, pady = 4)
bpow.bind("<Button-1>", click)
frame.pack()

root.mainloop()