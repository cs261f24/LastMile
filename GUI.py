import tkinter
import tkinter as tk
from tkinter import *

# Create main dashboard = tk.Tk()
dash = tk.Tk()
# window size
dash.geometry("1130x600")
# background color 
dash.configure(bg="white")
# title that appears at the top left of the windo
dash.title("DASHBOARD - V2")

# big frame at the top of the screen
topFrame = tk.Frame(
    dash
)
topFrame.pack(
    fill="both",
    expand=True
)

# two smaller frames in the big frame
section1 = tk.Frame(
    topFrame,
    bg="#89B68A"
)
section1.pack(
    padx=10,
    pady=10,
    side="left",
    fill="both",
    expand="True"
)

section2 = tk.Frame(
    topFrame,
    bg="#063970"
)
section2.pack(
    padx=10,
    pady=10,
    side="left",
    fill="both",
    expand="True"
)

# frame at the bottom half of the screen
bottomFrame = tk.Frame(
    dash,
    bg="#063970"
)
bottomFrame.pack(
    fill="both",
    expand=True,
)

# smaller frames for the days of the week
mon = tk.Frame(
    bottomFrame,
    bg="#89B68A",
    )
mon.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)

tue = tk.Frame(
    bottomFrame,
    bg="#89B68A"
    )
tue.pack(
    side="left",
    expand=True,
    fill="both",
    pady=5
)


wed = tk.Frame(
    bottomFrame,
    bg="#89B68A",
    )
wed.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)


thu = tk.Frame(
    bottomFrame,
    bg="#89B68A"
    )
thu.pack(
    side="left",
    expand=True,
    fill="both",
    pady=5
)


fri = tk.Frame(
    bottomFrame,
    bg="#89B68A",
    )
fri.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)


sat = tk.Frame(
    bottomFrame,
    bg="#89B68A"
    )
sat.pack(
    side="left",
    expand=True,
    fill="both",
    pady=5
)


fri = tk.Frame(
    bottomFrame,
    bg="#89B68A",
    )
fri.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)


# runs the code
dash.mainloop()