from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="Black")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17, bg="#fff", fg="Black", font=("Arial Bold", 28), textvariable=self.equation).place(x=0, y=0)
        
        self.create_button(master, "(", 0, 50, lambda: self.show("("))
        self.create_button(master, ")", 90, 50, lambda: self.show(")"))
        self.create_button(master, "%", 180, 50, lambda: self.show("%"))
        self.create_button(master, "1", 0, 125, lambda: self.show(1))
        self.create_button(master, "2", 90, 125, lambda: self.show(2))
        self.create_button(master, "3", 180, 125, lambda: self.show(3))
        self.create_button(master, "4", 0, 200, lambda: self.show(4))
        self.create_button(master, "5", 90, 200, lambda: self.show(5))
        self.create_button(master, "6", 180, 200, lambda: self.show(6))
        self.create_button(master, "7", 0, 275, lambda: self.show(7))
        self.create_button(master, "8", 180, 275, lambda: self.show(8))
        self.create_button(master, "9", 90, 275, lambda: self.show(9))
        self.create_button(master, "0", 90, 350, lambda: self.show(0))
        self.create_button(master, ".", 180, 350, lambda: self.show("."))
        self.create_button(master, "+", 270, 275, lambda: self.show("+"))
        self.create_button(master, "-", 270, 200, lambda: self.show("-"))
        self.create_button(master, "/", 270, 50, lambda: self.show("/"))
        self.create_button(master, "x", 270, 125, lambda: self.show("*"))
        self.create_button(master, "=", 270, 350, self.solve, bg="blue")
        self.create_button(master, "C", 0, 350, self.clear, bg="blue")
        
    def create_button(self, master, text, x, y, command, bg="White"):
        button = Button(master, width=11, height=4, text=text, relief="flat", bg=bg, command=command)
        button.place(x=x, y=y)
        button.bind("<Enter>", lambda event, b=button: b.config(bg="lightgrey"))
        button.bind("<Leave>", lambda event, b=button: b.config(bg=bg))

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()
