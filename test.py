import tkinter as tk



def display():

    if(x.get()==1):

        print("You agree!")

    else:

        print("You don't agree :(")



window = tk.Tk()

x = tk.IntVar()

check_button = tk.Checkbutton(window,

                           text="I agree to something",

                           variable=x,

                           onvalue=1,

                           offvalue=0,

                           command=display,

                           font=('Arial',20),

                           fg='#00FF00',

                           bg='black',

                           activeforeground='#00FF00',

                           activebackground='black',

                           padx=25,

                           pady=10,

                           compound='left')

check_button.pack()





window.mainloop()