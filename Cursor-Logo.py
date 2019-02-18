from tkinter import *
from tkinter import ttk
root = Tk()
def wait():
    root.config(cursor="wait")
    
def CROSSHAIR():
    root.config(cursor="CROSSHAIR")
def Close():
    root.destroy()
def Hand():
    root.config(cursor="boat")
def based_arrow_down():
    root.config(cursor="based_arrow_down")
def based_arrow_up():
    root.config(cursor="based_arrow_up")
def bogosity():
    root.config(cursor="bogosity")
def bottom_left_corner():
    root.config(cursor="bottom_left_corner")
def bottom_right_corner():
    root.config(cursor="bottom_right_corner")
def bottom_side():
    root.config(cursor="bottom_side")
def bottom_tee():
    root.config(cursor="bottom_tee")
def box_spiral():
    root.config(cursor="box_spiral")
def center_ptr():
    root.config(cursor="center_ptr")
def circle():
    root.config(cursor="circle")
def clock():
    root.config(cursor="clock")
def coffee_mug():
    root.config(cursor="coffee_mug")
def cross_reverse():
    root.config(cursor="cross_reverse")
def cross():
    root.config(cursor="cross")
def diamond_cross():
    root.config(cursor="diamond_cross")
def dot():
    root.config(cursor="dot")
def dotbox():
    root.config(cursor="dotbox")
def double_arrow():
    root.config(cursor="double_arrow")
def draft_large():
    root.config(cursor="draft_large")
def draft_small():
    root.config(cursor="draft_small")
def draped_box():
    root.config(cursor="draped_box")
def exchange():
    root.config(cursor="exchange")
def fleur():
    root.config(cursor="fleur")
def gobbler():
    root.config(cursor="gobbler")
def gumby():
    root.config(cursor="gumby")
def hand1():
    root.config(cursor="hand1")
def hand2():
    root.config(cursor="hand2")
def heart():
    root.config(cursor="heart")
def icon():
    root.config(cursor="icon")
def iron_cross():
    root.config(cursor="iron_cross")
def left_ptr():
    root.config(cursor="left_ptr")
def left_side():
    root.config(cursor="left_side")
def left_tee():
    root.config(cursor="left_tee")
def leftbutton():
    root.config(cursor="leftbutton")
def ll_angle():
    root.config(cursor="ll_angle")
def lr_angle():
    root.config(cursor="lr_angle")
def man():
    root.config(cursor="man")
def man():
    root.config(cursor="man")
def middlebutton():
    root.config(cursor="middlebutton")
def mouse():
    root.config(cursor="mouse")
def pencil():
    root.config(cursor="pencil")
def pirate():
    root.config(cursor="pirate")
def plus():
    root.config(cursor="plus")
def question_arrow():
    root.config(cursor="question_arrow")
def right_ptr():
    root.config(cursor="right_ptr")
def right_side():
    root.config(cursor="right_side")
ttk.Button(root, text="Wait", command=wait).grid(row = 1, column = 1)
ttk.Button(root, text="CROSSHAIR", command=CROSSHAIR).grid(row = 2, column = 1)
ttk.Button(root, text="boat", command=Hand).grid(row = 3, column = 1)
ttk.Button(root, text="based arrow down", command=based_arrow_down).grid(row = 4, column = 1)
ttk.Button(root, text="based arrow UP", command=based_arrow_up).grid(row = 5, column = 1)
ttk.Button(root, text="bogosity", command=bogosity).grid(row = 6, column = 1)
ttk.Button(root, text="bottom left_corner", command=bottom_left_corner).grid(row = 7, column = 1)
ttk.Button(root, text="bottom right corner", command=bottom_right_corner).grid(row = 8, column = 1)
ttk.Button(root, text="bottom side", command=bottom_side).grid(row = 9, column = 1)
ttk.Button(root, text="bottom tee", command=bottom_tee).grid(row = 10, column = 1)
ttk.Button(root, text="box spiral", command=box_spiral).grid(row = 11, column = 1)
ttk.Button(root, text="center ptr", command=center_ptr).grid(row = 12, column = 1)
ttk.Button(root, text="circle", command=circle).grid(row = 12, column = 1)
ttk.Button(root, text="clock", command=clock).grid(row = 12, column = 1)
ttk.Button(root, text="coffee mug", command=coffee_mug).grid(row = 13, column = 1)
ttk.Button(root, text="cross reverse", command=cross_reverse).grid(row = 14, column = 1)
ttk.Button(root, text="cross", command=cross).grid(row = 15, column = 1)
ttk.Button(root, text="diamond cross", command=dot).grid(row = 16, column = 1)
ttk.Button(root, text="dot", command=diamond_cross).grid(row = 17, column = 1)
ttk.Button(root, text="dotbox", command=dotbox).grid(row = 18, column = 1)
ttk.Button(root, text="double arrow", command=double_arrow).grid(row = 19, column = 1)
ttk.Button(root, text="draft small", command=draft_small).grid(row = 20, column = 1)
ttk.Button(root, text="draft large", command=draft_large).grid(row = 21, column = 1)
ttk.Button(root, text="draped box", command=draped_box).grid(row = 22, column = 1)
ttk.Button(root, text="exchange", command=exchange).grid(row = 23, column = 1)
ttk.Button(root, text="fleur", command=fleur).grid(row = 23, column = 1)
ttk.Button(root, text="gobbler", command=gobbler).grid(row = 24, column = 1)
ttk.Button(root, text="gumby", command=gumby).grid(row = 25, column = 1)
ttk.Button(root, text="hand1", command=hand1).grid(row = 26, column = 1)
ttk.Button(root, text="hand2", command=hand2).grid(row = 27, column = 1)
ttk.Button(root, text="heart", command=heart).grid(row = 28, column = 1)
ttk.Button(root, text="icon", command=icon).grid(row = 29, column = 1)
ttk.Button(root, text="iron cross", command=iron_cross).grid(row = 29, column = 1)
ttk.Button(root, text="left ptr", command=left_ptr).grid(row = 30, column = 1)
ttk.Button(root, text="left side", command=left_side).grid(row = 1, column = 2)
ttk.Button(root, text="left tee", command=left_tee).grid(row = 2, column = 2)
ttk.Button(root, text="leftbutton", command=leftbutton).grid(row = 3, column = 2)
ttk.Button(root, text="ll angle", command=ll_angle).grid(row = 3, column = 2)
ttk.Button(root, text="lr_angle", command=lr_angle).grid(row = 4, column = 2)
ttk.Button(root, text="man", command=man).grid(row = 5, column = 2)
ttk.Button(root, text="middlebutton", command=middlebutton).grid(row = 6, column = 2)
ttk.Button(root, text="mouse", command=mouse).grid(row = 7, column = 2)
ttk.Button(root, text="pencil", command=pencil).grid(row = 8, column = 2)
ttk.Button(root, text="pirate", command=pirate).grid(row = 9, column = 2)
ttk.Button(root, text="plus", command=plus).grid(row = 10, column = 2)
ttk.Button(root, text="question arrow", command=question_arrow).grid(row = 11, column = 2)
ttk.Button(root, text="right ptr", command=right_ptr).grid(row = 12, column = 2)
ttk.Button(root, text="right side", command=right_side).grid(row = 13, column = 2)
ttk.Button(root, text="Close", command=Close).grid(row = 30, column = 2)
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.destroy())
root.mainloop()
