from threading import Thread


def work():
    import tkinter as tk
    root = tk.Tk()
    root.title("Interpolation")
    root.geometry('700x700')


    Text_field = tk.Label(root, text="\nHow many relations of x\n and y do you have?", font=('arial', 20, 'bold'))
    Text_field.pack()
    inptxt = tk.Entry(root, justify="center", width = 5, font=('arial', 15, 'bold'));inptxt.pack()



    text_var = []
    matrix_entries = list()


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
    spc = '                            \n'*100
    tk.Label(scrollable_frame, text='(x,y)\n'+spc, font=('arial', 20)).pack()

    # tk.Label(scrollable_frame, text='\tx\t\ty\t').pack(side='top', anchor='e')



    to_check = tk.Label(root, text = 'f(?)', font = ('arial', 20))
    to_check.pack(side='bottom')
    X = tk.Entry(root, justify="center", width = 7, font=('arial', 15, 'bold'))
    X.pack(side='bottom')

    def direct_f():
        mat = list()
        for x in text_var:
            mat.append([0])
            for y in x:
                cc = y.get()
                try:
                    cc = float(cc)
                except:
                    cc = 0
                mat[-1].append(cc)
        
        # print(*mat, sep='\n')
        import Direct_Interpolation as di
        xx = X.get()
        try:
            xx = float(xx)
            di.run(mat, xx)
        except:
            print('f(?) !!!')

    def lag_f():
        mat = list()
        for x in text_var:
            mat.append([0])
            for y in x:
                cc = y.get()
                try:
                    cc = float(cc)
                except:
                    cc = 0
                mat[-1].append(cc)
        
        # print(*mat, sep='\n')
        import Lagrangian_Interpolation as li
        xx = X.get()
        try:
            xx = float(xx)
            li.run(mat, xx)
        except:
            print('f(?) !!!')

    def newt_f():
        mat = list()
        for x in text_var:
            mat.append([0])
            for y in x:
                cc = y.get()
                try:
                    cc = float(cc)
                except:
                    cc = 0
                mat[-1].append(cc)
        
        # print(*mat, sep='\n')
        import Newton_Interpolation as ni
        xx = X.get()
        try:
            xx = float(xx)
            ni.run(mat, xx)
        except Exception as e:
            print('f(?) !!!', e)

        

    dir_intrp = tk.Button(root, text='Direct', font=('arial', 20), command = direct_f)
    lag_intrp = tk.Button(root, text='Lagrangian', font=('arial', 20), command = lag_f)
    newton_intrp = tk.Button(root, text='Newton\'s', font=('arial', 20), command = newt_f)
    def take_input():
        t = inptxt.get()
        try:
            t = int(t)
            x2 = 0
            y2 = 23
            cols = 2
            for x in matrix_entries:
                for y in x:
                    y.destroy()
            matrix_entries.clear()
            text_var.clear()
            for i in range(t):
                text_var.append([])
                matrix_entries.append([])
                text_var[i].append(tk.StringVar(root))
                matrix_entries[i].append(tk.Entry(scrollable_frame, textvariable=text_var[i][0],width=25))
                text_var[i].append(tk.StringVar(root))
                matrix_entries[i][0].place(x = 0, y = 50+y2)
                matrix_entries[i].append(tk.Entry(scrollable_frame, textvariable=text_var[i][1], width = 15))
                matrix_entries[i][1].place(x = 100, y = 50+y2)



                y2 += 25
                x2 = 0

            container.pack(side='left')
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            dir_intrp.pack(side = 'bottom', anchor = 'e')
            lag_intrp.pack(side='bottom', anchor = 'e')
            newton_intrp.pack(side='bottom', anchor = 'e')
            # print(t)
        except Exception as e:
            print(e)
            dir_intrp.pack_forget()
            lag_intrp.pack_forget()
            newton_intrp.pack_forget()
            matrix_entries.clear()
            text_var.clear()
    testCase_button = tk.Button(root, text = 'OK', font=('arial', 15),  command = take_input)
    testCase_button.pack()

    tk.Label(text = '\n').pack()






    root.mainloop()


# work()
def run():
    Thread(target=work).start()
