from threading import Thread
from tkinter import *
from math import floor

def work():
    import tkinter as tk
    from matplotlib.figure import Figure
    import Regression as rg
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
    NavigationToolbar2Tk)
    import numpy as np





    xx = []
    yy = list()
    matrix_entries = list()
    prev_widget = list()

    def plot():
        for item in prev_widget:
            item.pack_forget()
        x = list()
        y = list()
        for i in range(len(xx)):
            a = xx[i].get()
            b = yy[i].get()
            try:
                a = float(a)
                b = float(b)
                x.append(a)
                y.append(b)
            except:
                break


        beta = rg.betaArr(x, y)
        beta1 = beta[0]
        beta2 = beta[1]

        print(beta1, beta2)


        # the figure that will contain the plot
        fig = Figure(figsize = (5, 5), dpi = 100)
        # adding the subplot
        plot1 = fig.add_subplot(111)
        plot1.set_xlabel("X axis")
        plot1.set_ylabel("Y axis")
        a=x
        b=y
        mn = floor(min(x))
        mx = floor(max(x))+1

        x = np.array(range(mn,mx))
        # beta1 = -1.2
        # beta2 = 8
        y = x * beta1 + beta2
        c = ''
        if beta2 > 0:
            c = '+'+str(beta2)
        elif beta2 == 0:
            c = ''
        else:
            c = str(beta2)


        # plotting the graph
        plot1.plot(x,y,label=('y='+str(beta1)+'x'+c))
        plot1.plot(a,b,label='Original')
        plot1.legend()
        # plot1.show()

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = root)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().place(x=400,y=100)
        prev_widget.append(canvas.get_tk_widget())

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                    root)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
        prev_widget.append(canvas.get_tk_widget())
        prev_widget.append(toolbar)

    # the main Tkinter window
    root = Tk()


    # setting the title
    root.title('Linear Regression')


    # dimensions of the main window
    root.geometry("900x500")




    from tkinter import ttk
    container = ttk.Frame(root)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)


    x2 = 0
    y2 = 23
    cols = 2

    spc = '                            \n'*100
    tk.Label(root, text = 'Insert your data as you wish, \nfill them from the first row \nsequentially according to your\n need, you can keep the \nrest of the table blank\n.').place(x=10,y=10)
    tk.Label(scrollable_frame, text='(x,y)\n'+spc, font=('arial', 20)).pack()
    for i in range(200):
        matrix_entries.append([])
        xx.append(tk.StringVar(root))
        matrix_entries[i].append(tk.Entry(scrollable_frame, textvariable=xx[i],width=25))
        yy.append(tk.StringVar(root))
        matrix_entries[i][0].place(x=0, y =50+y2)
        matrix_entries[i].append(tk.Entry(scrollable_frame, textvariable=yy[i], width = 15))
        matrix_entries[i][1].place(x=100, y=50+y2)
        y2 += 20
        x2 = 0







    container.pack(side = 'left')
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")







    # button that displays the plot
    plot_button = Button(master = root,
                        command = plot,
                        height = 2,
                        width = 10,
                        text = "Plot")





    # place the button
    # in main window
    plot_button.pack()

    # run the gui
    root.mainloop()

def run():
    Thread(target=work).start()
