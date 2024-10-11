from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import math
import matplotlib.pyplot as plt

# globally declare the expression variable 
expression = "" 

# function for press 
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 

# Function to evaluate the final expression 
def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = ""

# Function to clear the contents 
def clear(): 
    global expression 
    expression = "" 
    equation.set("")

# Function to graph the input values
def graph_input():
    try:
        x_label = simpledialog.askstring("Input", "Enter label for X-axis:")
        y_label = simpledialog.askstring("Input", "Enter label for Y-axis:")
        x_values = simpledialog.askstring("Input", "Enter X values separated by commas:")
        y_values = simpledialog.askstring("", "Enter Y values separated by commas:")
        
        x = [float(i) for i in x_values.split(',')]
        y = [float(i) for i in y_values.split(',')]
        
        if len(x) != len(y):
            messagebox.showerror("Error", "X and Y values must have the same number of elements!")
            return
        
        plt.figure()
        plt.plot(x, y, marker='o')
        plt.title("Graph of Y vs X")
        plt.xlabel(x_label if x_label else "X values")
        plt.ylabel(y_label if y_label else "Y values")
        plt.grid()
        plt.show()
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function for scientific operations
def scientific_operation(func):
    try:
        global expression
        expression = str(func(float(expression)))
        equation.set(expression)
    except:
        equation.set(" error ")
        expression = ""

# Driver code 
if __name__ == "__main__": 
    gui = Tk() 
    gui.title("Scientific Calculator") 
    gui.configure(background="darkslategray") 
    gui.geometry("300x310") 
    gui.resizable(False, False)

    equation = StringVar() 

    expression_field = Entry(gui, textvariable=equation, font=('Arial', 14), bd=5, insertwidth=4, width=20, borderwidth=4)
    expression_field.grid(columnspan=4, ipadx=8)

    button_style = {
        'font': ('Arial', 12),
        'bd': 5,
        'width': 5,
        'bg': '#282c34',  # Dark background for buttons
        'fg': '#61dafb'   # Light foreground color
    }

    # Creating standard calculator buttons
    button1 = Button(gui, text=' 1 ', command=lambda: press(1), **button_style)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', command=lambda: press(2), **button_style)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', command=lambda: press(3), **button_style)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', command=lambda: press(4), **button_style)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', command=lambda: press(5), **button_style)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', command=lambda: press(6), **button_style)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', command=lambda: press(7), **button_style)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', command=lambda: press(8), **button_style)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', command=lambda: press(9), **button_style)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', command=lambda: press(0), **button_style)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', command=lambda: press("+"), **button_style)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', command=lambda: press("-"), **button_style)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', command=lambda: press("*"), **button_style)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', command=lambda: press("/"), **button_style)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', command=equalpress, **button_style)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', command=clear, **button_style)
    clear.grid(row=5, column=1)

    Decimal = Button(gui, text='.', command=lambda: press('.'), **button_style)
    Decimal.grid(row=6, column=0)

    # Adding scientific function buttons
    sin_button = Button(gui, text='sin', command=lambda: scientific_operation(math.sin), **button_style)
    sin_button.grid(row=6, column=1)

    cos_button = Button(gui, text='cos', command=lambda: scientific_operation(math.cos), **button_style)
    cos_button.grid(row=6, column=2)

    tan_button = Button(gui, text='tan', command=lambda: scientific_operation(math.tan), **button_style)
    tan_button.grid(row=6, column=3)

    log_button = Button(gui, text='log', command=lambda: scientific_operation(math.log), **button_style)
    log_button.grid(row=7, column=0)

    sqrt_button = Button(gui, text='√', command=lambda: scientific_operation(math.sqrt), **button_style)
    sqrt_button.grid(row=7, column=1)

    exp_button = Button(gui, text='exp', command=lambda: scientific_operation(math.exp), **button_style)
    exp_button.grid(row=7, column=2)

    # Button for graphing
    graph_button = Button(gui, text='Graph', command=graph_input, font=('Arial', 12), bd=5, width=10, bg='#f44336', fg='white')
    graph_button.grid(row=7, column=3)

    # Start the GUI 
    gui.mainloop()
