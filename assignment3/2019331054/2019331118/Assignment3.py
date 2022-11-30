import tkinter as tk
import Gui_Regression as erk
import Interpolation as intg
top = tk.Tk()
top.title("Solve function")
top.geometry('400x300')
arial = ('arial', 20)

def regression():
    erk.run()
def interpolation():
    intg.run()
tk.Label(top, text='\n', font = arial).pack()
tk.Button(top, text = 'Interpolation', bg='green', fg='white', activebackground='black', activeforeground='white', font = arial, command = interpolation).pack(pady = 10)
tk.Button(top, text = 'Regression Model', bg='green', fg='white', font = arial, activebackground='black', activeforeground='white', command = regression).pack(pady =1)


top.mainloop()