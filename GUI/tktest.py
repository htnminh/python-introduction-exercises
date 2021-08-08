import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()


label = tk.Label(
    text="Hello, Tkinter",
    foreground="red",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10,
    height=10,
)
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()


starting = tk.Label(text="Start of sum of 2 integers:",
                    width=30,
                    height=5,)
starting.pack()

int1 = tk.Entry()
int1.pack()

int2 = tk.Entry()
int2.pack()

def start_sum():
    num1 = int(int1.get())
    num2 = int(int2.get())
    sum_box = tk.Label(text = str(num1 + num2))
    sum_box.pack()
    
button = tk.Button(
    text="Calculate sum!",
    width=25,
    height=2,
    command = start_sum
)
button.pack()
