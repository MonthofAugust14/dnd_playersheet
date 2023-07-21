import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

frame = tk.LabelFrame(window, text="Labelframe test")
frame.grid(row=0, column=0)

button = tk.Button(frame, text="Test", font=("", 100))
button.grid(row=0, column=0, sticky="news")
button2 = tk.Button(frame, text="Test2", font=("", 100))
button2.grid(row=1, column=1, sticky="news")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(1, weight=1)


window.mainloop()