import time
from tkinter import *
from PIL import Image, ImageTk
import pyttsx3
from tkterminal import Terminal

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
win_width = 300
win_height = 500
x = int((screen_width/2) - (win_width/2))
y = int((screen_height/2) - (win_height/2))

root.geometry(f"{win_width}x{win_height}+{x}+{y}")
root.overrideredirect(True)

load_img = Image.open("Images\\robot2.jpg")
resized_img = load_img.resize((300, 500), Image.Resampling.LANCZOS)
bg = ImageTk.PhotoImage(resized_img)

my_canvas = Canvas(root, width=300, height=500, bg="lightblue", bd=0, highlightthickness=0)
my_canvas.pack()
my_canvas.create_image(0, 0, anchor="nw", image=bg)

us_entry = Entry(root, width=15, font=("Fixedsys" ,18), fg="#007fd8")
pwd_entry = Entry(root, width=15, font=("Fixedsys",18), fg="#007fd8")
us_entry.insert(0, "Username")
pwd_entry.insert(0, "Password")
my_canvas.create_window(27, 40, anchor="nw", window=us_entry)
my_canvas.create_window(27, 90, anchor="nw", window=pwd_entry)

def SAR1_win():
    win = Tk()
    win.geometry('300x300')

    sc_width = win.winfo_screenwidth()
    sc_height = win.winfo_screenheight()

    win.title("AI")
    win.attributes('-fullscreen', 'True')

    load_winimg = Image.open('Images\\HDAI.jpg')
    resized_winimg = load_winimg.resize((sc_width, sc_height), Image.Resampling.LANCZOS)
    win_bg = ImageTk.PhotoImage(resized_winimg)

    win_canvas = Canvas(win, width=sc_width, height=sc_height, bd=0, highlightthickness=0)
    win_canvas.pack()
    win_canvas.create_image(0, 0, anchor='nw', image=win_bg)

    win_btn = Button(win, text="Exit", font=("Fixedsys", 25),fg="cyan",bg="black", height=1,width=10,bd=0,command=win.destroy)
    win_btn.pack()
    win_canvas.create_window(10, 720, anchor='nw', window=win_btn)

    def my_clock():
        hour, minute, second = time.strftime("%H"), time.strftime("%M"), time.strftime("%S")
        date, month, year = time.strftime("%d"), time.strftime("%b"), time.strftime("%y")
        day = time.strftime("%A")
        
        clock_label.config(text=f"{hour}:{minute}:{second}")
        clock_label.after(1000, my_clock)

        date_label.config(text=f"{date}/{month}/{year}")

        day_label.config(text=day)
        

    clock_label = Label(win, text ="",bg="black", fg="cyan", font=("Terminal", 30), width=9)
    clock_label.pack(pady=30)
    win_canvas.create_window(10, 10, anchor='nw', window=clock_label)

    date_label = Label(win, text ="",bg="black", fg="cyan", font=("Fixedsys", 30), width=9)
    date_label.pack()
    win_canvas.create_window(1340, 10, anchor='nw', window=date_label)

    day_label = Label(win, text="", font=("System", 25), fg="cyan", bg="black", width=9)
    day_label.pack()
    win_canvas.create_window(1340, 60, anchor='nw', window=day_label)

    my_terminal = Terminal(win, width=30, height=10, font=("Fixedsys", 21),bg="black", fg="cyan", state=NORMAL, wrap=WORD)
    my_terminal.pack()
    win_canvas.create_window(250, 250, anchor='nw', window=my_terminal)
    my_terminal.shell = True
    my_terminal.basename = ">>"
    my_terminal.tag_config("output", foreground="cyan")
    my_terminal.tag_config("basename", foreground="cyan")

    my_clock()


    win.mainloop()

def SAR2_win():
    win = Tk()

    sc_width = win.winfo_screenwidth()
    sc_height = win.winfo_screenheight()

    win.title("AI")
    win.attributes('-fullscreen', 'True')


    load_winimg = Image.open('Images\\HDAI2.jpg')
    resized_winimg = load_winimg.resize((sc_width, sc_height), Image.Resampling.LANCZOS)
    win_bg = ImageTk.PhotoImage(resized_winimg)

    win_canvas = Canvas(win, width=sc_width, height=sc_height, bd=0, highlightthickness=0)
    win_canvas.pack()
    win_canvas.create_image(0, 0, anchor='nw', image=win_bg)

    win_btn = Button(win, text="Exit", font="Helvetica 20 bold",fg="#24bdc7",bg="white", height=1,width=20,bd=0,command=win.destroy)
    win_btn.pack()
    win_canvas.create_window(150, 600, anchor='nw', window=win_btn)

    win.mainloop()

def welcome():
    pwd_list = ["rehan", "saiyyam", "apoorva"]
    if us_entry.get() == "SAR1" and pwd_entry.get() in pwd_list:
        engine.setProperty('voice', voices[0].id)
        speak("Welcome to SAR1")
        root.destroy()

        SAR1_win()
    elif us_entry.get() == "SAR2" and pwd_entry.get() in pwd_list:
        engine.setProperty('voice',voices[1].id)
        speak("Welcome to SAR2")
        root.destroy()

        SAR2_win()
    else:
        speak("Invalid Password")
    
login_btn = Button(root, text="Login", font="Fixedsys 18 bold" ,width=6, bd=2, fg="#007fd8", command=welcome)
my_canvas.create_window(90, 160, anchor="nw", window=login_btn)

def entry_clear(e):
    if us_entry.get() == "Username" and pwd_entry.get() == "Password":
        us_entry.delete(0, END)
        pwd_entry.delete(0, END)
        pwd_entry.config(show="*")

us_entry.bind("<Button-1>", entry_clear)
pwd_entry.bind("<Button-1>", entry_clear)


speak("Enter Password")


root.mainloop()