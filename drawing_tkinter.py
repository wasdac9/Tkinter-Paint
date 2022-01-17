from tkinter import *
import tkinter as tk

h=1080
w=1920


class Draw:
    def __init__(self):
        self.color="black"
        self.width = 10
        self.previous_x=0
        self.previous_y=0

    def draw_cirlces(self,event):
        self.event = event
        d = self.width/2
        canvas.create_oval(self.event.x-d, self.event.y-d, self.event.x+d,
                            self.event.y+d,fill=self.color,outline=self.color)

        if self.previous_x == 0 and self.previous_y == 0:
            self.previous_x,self.previous_y = self.event.x,self.event.y
            canvas.create_line(self.previous_x,self.previous_y, self.event.x,self.event.y,
                                width=self.width,fill=self.color)
        else:
            canvas.create_line(self.previous_x,self.previous_y, self.event.x,self.event.y,
                                width=self.width,fill=self.color)
            self.previous_x,self.previous_y = self.event.x,self.event.y

    def set_attributes(self,color="",width=10):
        if color == "":
            self.color = self.color
        else:
            self.color=color
        self.width = width

    def reset_draw(self,event):
        self.previous_x=0
        self.previous_y=0

draw = Draw()
root = tk.Tk()

canvas = tk.Canvas(root,height=h, width=w, bg="white")
red_button = Button(root,bg="red",command= lambda: draw.set_attributes(color="red"))
red_button.place(relx=0,rely=0,relwidth=0.1,relheight=0.1)
green_button = Button(root,bg="green",command= lambda: draw.set_attributes(color="green"))
green_button.place(relx=0.1,rely=0,relwidth=0.1,relheight=0.1)
blue_button = Button(root,bg="blue",command= lambda: draw.set_attributes(color="blue"))
blue_button.place(relx=0.2,rely=0,relwidth=0.1,relheight=0.1)
black_button = Button(root,bg="black",command= lambda: draw.set_attributes(color="black"))
black_button.place(relx=0.3,rely=0,relwidth=0.1,relheight=0.1)
white_button = Button(root,bg="gray",command= lambda: draw.set_attributes(color="white",width=30))
white_button.place(relx=0.4,rely=0,relwidth=0.1,relheight=0.1)
thickness_5 = Button(root,text="Thickness:5",bg="gray",command= lambda: draw.set_attributes(width=5))
thickness_5.place(relx=0.5,rely=0,relwidth=0.1,relheight=0.033)
thickness_10 = Button(root,text="Thickness:10",bg="gray",command= lambda: draw.set_attributes(width=10))
thickness_10.place(relx=0.5,rely=0.033,relwidth=0.1,relheight=0.033)
thickness_20 = Button(root,text="Thickness:20",bg="gray",command= lambda: draw.set_attributes(width=20))
thickness_20.place(relx=0.5,rely=0.066,relwidth=0.1,relheight=0.033)
canvas.pack()
#label = Label(root)
#label.pack()
canvas.bind("<B1-Motion>", lambda i: draw.draw_cirlces(i))
canvas.bind("<ButtonRelease-1>", lambda i: draw.reset_draw(i))


mainloop()
