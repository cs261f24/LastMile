from tkinter import *  # import classes and functions
import tkinter
import tkinter as tk  # allows Tkinter to be replaced with tk for short

# create dashboard and the dashboard name (dash)
dash = tk.Tk()

# Size of dashboard in pixels (I think)
dash.geometry("1130x600")

# Dash background color
dash.configure(bg="white")

# The title of the dashboard when the screen shows up
dash.title("DASHBOARD")


# creates a frame
# A frame is a section in which widgets are placed
# I made one for each day since I did not know how to use classes
mon = tk.LabelFrame(
    dash,
    bg="#063970",
    width=150,
    height=300,
)
mon.place(  # cordinates for the block
    x=10,
    y=290
)
mon.pack_propagate(0)  # creates and places the block
monlabel = tk.Label(  # creates text within the widget
    mon,  #location of text is in mon (the frame)
    text="MONDAY",
).place(  # places the text box in the coords
    x=40,
    y=10
)


tue = tk.Frame(
    dash,
    bg="#89B68A",
    width=150,
    height=300,
)
tue.place(
    x=170,
    y=290
)
tue.pack_propagate(0)
tuelabel = tk.Label(
    tue,
    text="TUESDAY",
).place(
    x=45,
    y=10
)


wed = tk.Frame(
    dash,
    bg="#063970",
    width=150,
    height=300,
)
wed.place(
    x=330,
    y=290
)
wed.pack_propagate(0)
monlabel = tk.Label(
    wed,
    text="WEDNESDAY",
).place(
    x=35,
    y=10
)

thu = tk.Frame(
    dash,
    bg="#89B68A",
    width=150,
    height=300,
)
thu.place(
    x=490,
    y=290
)
thu.pack_propagate(0)
thulabel = tk.Label(
    thu,
    text="THURSDAY",
).place(
    x=45,
    y=10
)


fri = tk.Frame(
    dash,
    bg="#063970",
    width=150,
    height=300,
)
fri.place(
    x=650,
    y=290
)
fri.pack_propagate(0)
frilabel = tk.Label(
    fri,
    text="FRIDAY",
).place(
    x=50,
    y=10
)

sat = tk.Frame(
    dash,
    bg="#89B68A",
    width=150,
    height=300,
)
sat.place(
    x=810,
    y=290
)
sat.pack_propagate(0)
monlabel = tk.Label(
    sat,
    text="SATURDAY",
).place(
    x=45,
    y=10
)

sun = tk.Frame(
    dash,
    bg="#063970",
    width=150,
    height=300,
)
sun.place(
    x=970,
    y=290
)
sun.pack_propagate(0)
sunlabel = tk.Label(
    sun,
    text="SUNDAY",
).place(
    x=45,
    y=10
)

# Big frame on top

Main_Dash = tk.Frame(
    dash,
    bg="#063970",
    width=1110,
    height=275,
)
Main_Dash.place(
    x=10,
    y=10
)

# this line will actually run all code above
dash.mainloop()
