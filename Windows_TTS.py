import tkinter as tk

win = tk.Tk()
win.title("TTS_Windows")
win.geometry("640x480")

label_Name = tk.Label(win, text="The program that translates txt files into mp3")
label_Name.pack()

win.mainloop()