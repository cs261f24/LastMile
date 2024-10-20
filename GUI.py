import tkinter
from tkinter import *
import tkinter as tk

# Create main dashboard = tk.Tk()
dash = tk.Tk()
# window size
dash.geometry("1130x600")
# background color
dash.configure(bg="#a2cf8c")
# title that appears at the top left of the windo
dash.title("Last Mile Dashboard")

# image pathing does not work currently, it requires entire path
# pic = tk.PhotoImage(image="images.png")
# dash.iconphoto(True, pic)

# ------------------------------------------------------------------------------------------
# Day screen 
today = tk.Frame(
    dash,
    height=20,
    bg="#a2cf8c"
)
today.pack(
    side="top",
    fill="both",
)
daylabel = tk.Label(
    today,
    text="Todays Date",
    bg="#a2cf8c",
    font=("Arial", 20)
)
daylabel.pack(
    pady=5,
    side="top"
)

# -----------------------------------------------------------------------------------------------
# big frame at the top of the screen
LeftMainFrame = tk.Frame(
    dash,
    bg="#213f69"
)
LeftMainFrame.pack(
    fill="both",
    expand="True"
)

# -------------------------------------------------------------------------------------------------
# three smaller frames in the big frame

# section 1 is the weather

section1 = tk.Frame(
    LeftMainFrame,
    bg="#a2cf8c"
)
section1.pack(
    padx=5,
    pady=5,
    side="left",
    fill="both",
    expand=True
)
section1.pack_propagate(False)

wheatherCond = tk.Label(
    section1,
    text="Sunny",
    bg="#a2cf8c",
    font=("Times", 30)
)
wheatherCond.pack(
    pady=10,
)
tempAlert = tk.Label(
    section1,
    text="BLACK ICE",
    bg="#a2cf8c",
    font=(30)
)
tempAlert.pack(
    pady=5,
)
tempHigh = tk.Label(
    section1,
    text="H: " + "90",
    bg="#a2cf8c",
    font=(30)
)
tempHigh.pack(
    pady=5,
)

tempLow = tk.Label(
    section1,
    text="L: " + "-3",
    bg="#a2cf8c",
    font=(30)
)
tempLow.pack(
    pady=5,
)

# --------------------------------------------------------------------------------------------

# section 2 will be traffic

section2 = tk.Frame(
    LeftMainFrame,
    bg="#a2cf8c"
)
section2.pack(
    padx=5,
    pady=5,
    side="left",
    fill="both",
    expand=True
)
section2.pack_propagate(False)

trafficCond = tk.Label(
    section2,
    text="Game Day",
    bg="#a2cf8c",
    font=("Times", 30)
)
trafficCond.pack(
    pady=10,
)
games = tk.Label(
    section2,
    text="game info",
    bg="#a2cf8c",
    font=("Times", 25)
)
games.pack(
    pady=10,
)

# ---------------------------------------------------------------------------------------------

# section 3 are volunter predictions for the CURRENT day

section3 = tk.Frame(
    LeftMainFrame,
    bg="#a2cf8c",
)
section3.pack(
    pady=5,
    padx=5,
    side="left",
    fill="both",
    expand=True
)
section3.pack_propagate(False)

volunteerPred = tk.Label(
    section3,
    text="Est. " + "?? " + "volunteers",
    bg="#a2cf8c",
    font=("Times", 20)
)
volunteerPred.pack(
    pady=10,
)
totalVolunteers = tk.Label(
    section3,
    text="# total",
    bg="#a2cf8c",
    font=("Times", 20)
)
totalVolunteers.pack(
    pady=10,
)
AbsentVolunteers = tk.Label(
    section3,
    text="Expect " + "# " + "Absent",
    bg="#a2cf8c",
    font=("Times", 20)
)
AbsentVolunteers.pack(
    pady=10,
)

# ----------------------------------------------------------------------------------------------

# Section 4 is the RESCUE DATA

section4 = tk.Frame(
    LeftMainFrame,
    bg="#a2cf8c",
)
section4.pack(
    pady=5,
    padx=5,
    side="right",
    fill="both",
    expand=True
)
section4.pack_propagate(False)

rescues = tk.Label(
    section4,
    text="Est. " "#" + " Rescues",
    bg="#a2cf8c",
    font=("Times", 20)
)
rescues.pack(
    pady=10,
)
donations = tk.Label(
    section4,
    text="# of dono" + " Donations today",
    bg="#a2cf8c",
    font=("Times", 15)
)
donations.pack(
    pady=10,
)

# ------------------------------------------------------------------------------------------

# frame at the bottom half of the screen

bottomFrame = tk.Frame(
    dash,
    bg="#213f69"
)
bottomFrame.pack(
    fill="both",
    expand=True,
)

# -------------------------------------------------------------------------------------------

# smaller frames for the days of the week
day1 = tk.Frame(
    bottomFrame,
    bg="#a2cf8c",
    )
day1.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)
day1.pack_propagate(False)
day1date = tk.Label(
    day1,
    text="\u26C8 Date", wraplength=150,
    bg="#a2cf8c",
    font=("Times", 20)
)
day1date.pack(
    pady=10,
)
day1Hazard = tk.Label(
    day1,
    text="ICY ROADS",
    bg="#a2cf8c",
    font=("Times", 15)
)
day1Hazard.pack(  
    pady=3 
)
day1High = tk.Label(
    day1,
    text="H: " + "an Int",
    bg="#a2cf8c",
    font=("Times", 15)
)
day1High.pack(
    pady=3
)
day1Est = tk.Label(
    day1,
    text="15" + " / " "30 Volunteers",
    bg="#a2cf8c",
    font=("Times", 15)
)
day1Est.pack(
    pady=3
)


day2 = tk.Frame(
    bottomFrame,
    bg="#a2cf8c"
    )
day2.pack(
    side="left",
    expand=True,
    fill="both",
    pady=5
)
day2.pack_propagate(False)
day2date = tk.Label(
    day2,
    text="\u26C8 Date", wraplength=150,
    bg="#a2cf8c",
    font=("Times", 20)
)
day2date.pack(
    pady=10,
)
day2Hazard = tk.Label(
    day2,
    text="NONE",
    bg="#a2cf8c",
    font=("Times", 15)
)
day2Hazard.pack(
    pady=3
)
day2High = tk.Label(
    day2,
    text="H: " + "an Int",
    bg="#a2cf8c",
    font=("Times", 15)
)
day2High.pack(
    pady=3
)
day2Est = tk.Label(
    day2,
    text="15" + " / " "30 Volunteers",
    bg="#a2cf8c",
    font=("Times", 15)
)
day2Est.pack(
    pady=3
)


day3 = tk.Frame(
    bottomFrame,
    bg="#a2cf8c",
    )
day3.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)
day3.pack_propagate(False)
day3date = tk.Label(
    day3,
    text="\u26C8 Date", wraplength=150,
    bg="#a2cf8c",
    font=("Times", 20)
)
day3date.pack(
    pady=10,
)
day3Hazard = tk.Label(
    day3,
    text="NONE",
    bg="#a2cf8c",
    font=("Times", 15)
)
day3Hazard.pack(
    pady=3
)
day3High = tk.Label(
    day3,
    text="H: " + "an Int",
    bg="#a2cf8c",
    font=("Times", 15)
)
day3High.pack(
    pady=3
)
day3Est = tk.Label(
    day3,
    text="15" + " / " "30 Volunteers",
    bg="#a2cf8c",
    font=("Times", 15)
)
day3Est.pack(
    pady=3
)


day4 = tk.Frame(
    bottomFrame,
    bg="#a2cf8c"
    )
day4.pack(
    side="left",
    expand=True,
    fill="both",
    pady=5
)
day4.pack_propagate(False)
day4date = tk.Label(
    day4,
    text="\u26C8 Date", wraplength=150,
    bg="#a2cf8c",
    font=("Times", 20)
)
day4date.pack(
    pady=10,
)
day4Hazard = tk.Label(
    day4,
    text="NONE",
    bg="#a2cf8c",
    font=("Times", 15)
)
day4Hazard.pack(
    pady=3
)
day4High = tk.Label(
    day4,
    text="H: " + "an Int",
    bg="#a2cf8c",
    font=("Times", 15)
)
day4High.pack(
    pady=3
)
day4Est = tk.Label(
    day4,
    text="15" + " / " "30 Volunteers",
    bg="#a2cf8c",
    font=("Times", 15)
)
day4Est.pack(
    pady=3
)


day5 = tk.Frame(
    bottomFrame,
    bg="#a2cf8c",
    )
day5.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)
day5.pack_propagate(False)
day5date = tk.Label(
    day5,
    text="\u26C8 Date", wraplength=150,
    bg="#a2cf8c",
    font=("Times", 20)
)
day5date.pack(
    pady=10,
)
day5Hazard = tk.Label(
    day5,
    text="NONE",
    bg="#a2cf8c",
    font=("Times", 15)
)
day5Hazard.pack(
    pady=3
)
day5High = tk.Label(
    day5,
    text="H: " + "an Int",
    bg="#a2cf8c",
    font=("Times", 15)
)
day5High.pack(
    pady=3
)
day5Est = tk.Label(
    day5,
    text="15" + " / " "30 Volunteers",
    bg="#a2cf8c",
    font=("Times", 15)
)
day5Est.pack(
    pady=3
)


day6 = tk.Frame(
    bottomFrame,
    bg="#a2cf8c",
    )
day6.pack(
    side="left",
    expand=True,
    fill="both",
    pady=5
)
day6.pack_propagate(False)
day6date = tk.Label(
    day6,
    text="\u26C8 Date", wraplength=150,
    bg="#a2cf8c",
    font=("Times", 20)
)
day6date.pack(
    pady=10,
)
day6Hazard = tk.Label(
    day6,
    text="NONE",
    bg="#a2cf8c",
    font=("Times", 15)
)
day6Hazard.pack(
    pady=3
)
day6High = tk.Label(
    day6,
    text="H: " + "an Int",
    bg="#a2cf8c",
    font=("Times", 15)
)
day6High.pack(
    pady=3
)
day6Est = tk.Label(
    day6,
    text="15" + " / " "30 Volunteers",
    bg="#a2cf8c",
    font=("Times", 15)
)
day6Est.pack(
    pady=3
)


day7 = tk.Frame(
    bottomFrame,
    bg="#a2cf8c",
    )
day7.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=5
)
day7.pack_propagate(False)
day7date = tk.Label(
    day7,
    text="\u26C8 Date", wraplength=150,
    bg="#a2cf8c",
    font=("Times", 20)
)
day7date.pack(
    pady=10,
)
day7Hazard = tk.Label(
    day7,
    text="NONE",
    bg="#a2cf8c",
    font=("Times", 15)
)
day7Hazard.pack(
    pady=3
)
day7High = tk.Label(
    day7,
    text="H: " + "an Int",
    bg="#a2cf8c",
    font=("Times", 15)
)
day7High.pack(
    pady=3
)
day7Est = tk.Label(
    day7,
    text="15" + " / " "30 Volunteers",
    bg="#a2cf8c",
    font=("Times", 15)
)
day7Est.pack(
    pady=3
)


# runs the code
dash.mainloop()

# UNUSED: Will be used when program is turned into an actual application
# It will change the taskbar display:
# myappid = 'mycompany.myproduct.subproduct.version'
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
