import tkinter as tk
from tkinter import ttk
import pyttsx3

tts = pyttsx3.init()
voice = tts.getProperty("voices")
list_voice =[]
for i in voice:
    list_voice.append(i.name)

def set_voice():
    name_v = voice_menu.get()
    for vc in voice:
        if vc.name == name_v:
            tts.setProperty("voice", vc.id)

def save_mp3():
    file_name = Ent.get()
    file_save = EntF.get()
    with open(f"{file_name}", "r", encoding="utf-8") as file:
        files = file.read()
    tts.save_to_file(files, file_save)
    tts.runAndWait()

win = tk.Tk()
win.title("Windows_TTS")
win.geometry("480x300")

label_Name = tk.Label(win, text="The program that translates txt files into mp3")
label_Name.pack()

label_rfile = tk.Label(win, text="Specify the path to the file")
label_rfile.pack()

Ent = tk.Entry(win, width=45)
Ent.pack()

label_menu = tk.Label(win, text="Select a voice for text-to-speech")
label_menu.pack()

voice_menu = ttk.Combobox(win, values=list_voice, width=45)
voice_menu.current(0)
voice_menu.pack()

btn_set_voice = tk.Button(text="Set voice", command=set_voice)
btn_set_voice.pack()

save_label = tk.Label(text="Enter the address and name to save the file")
save_label.pack()

EntF = tk.Entry(win, width=45)
EntF.pack()

btn_save = tk.Button(text="Save mp3", command=save_mp3)
btn_save.pack()

win.mainloop()