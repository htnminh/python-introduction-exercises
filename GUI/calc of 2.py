import tkinter as tk
import tkinter.messagebox
import tkinter.ttk

starting = tk.Label(text="Sum of 2 integers",
                    width=30,
                    height=3,)
starting.pack()

cbb = tkinter.ttk.Combobox(state="readonly", values = ['+', '-', '*', '/'])
cbb.current(0)
cbb.pack()

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
        oper = cbb.get() # +
        calc_s = num1 + oper + num2
        #print(calc_s)
        num1 = int(num1) 
        num2 = int(num2)
        
        if oper in ['+', '-', '*']:
            res_box = tk.Label(text = '%i %s %i = %i'\
                           % (num1, oper, num2, eval(calc_s)))
            res_box.pack()
            tkinter.messagebox.showinfo('Result!', message='%i %s %i = %i'\
                           % (num1, oper, num2, eval(calc_s)))
        else:
            res_box = tk.Label(text = '%i %s %i = %.5f'\
                           % (num1, oper, num2, eval(calc_s)))
            res_box.pack()
            tkinter.messagebox.showinfo('Result!', message='%i %s %i = %f'\
                           % (num1, oper, num2, eval(calc_s)))
        
    except:
        error_box = tk.Label(text="%s %s %s : %s"\
                             % (num1, oper, num2, 'Invalid input(s)!'))
        error_box.pack()
        tkinter.messagebox.showerror(title = 'Error!', message= "%s %s %s : %s"\
                             % (num1, oper, num2, 'Invalid input(s)!'))
        
button = tk.Button(
    text="Calculate!",
    width=25,
    height=2,
    command = start_sum
)
button.pack()
