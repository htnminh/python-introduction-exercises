import tkinter as tk
import tkinter.messagebox

starting = tk.Label(text="Sum of 2 integers",
                    width=30,
                    height=3,)
starting.pack()

frame1 = tk.Frame()
label1 = tk.Label(master = frame1, text = 'First integer:')
label1.pack(side = 'left')
int1 = tk.Entry(master = frame1)
int1.pack()
frame1.pack()

frame2 = tk.Frame()
label2 = tk.Label(master = frame2, text = 'Second integer:')
label2.pack(side = 'left')
int2 = tk.Entry(master = frame2)
int2.pack()
frame2.pack()

def start_sum():
    num1 = int1.get()
    num2 = int2.get()
    try:
        num1 = int(num1)
        num2 = int(num2)
        sum_box = tk.Label(text = '%i + %i = %i'\
                           % (num1, num2, num1+num2))
        sum_box.pack()
        tk.messagebox.showinfo('Result!', message='%i + %i = %i'\
                           % (num1, num2, num1+num2))
    except:
        error_box = tk.Label(text="%s + %s : %s"\
                             % (num1, num2, 'Invalid input(s)!'))
        error_box.pack()
        tk.messagebox.showerror(title = 'Error!', message= "%s + %s : %s"\
                             % (num1, num2, 'Invalid input(s)!'))
        
button = tk.Button(
    text="Calculate sum!",
    width=25,
    height=2,
    command = start_sum
)
button.pack()