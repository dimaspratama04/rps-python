# Modules
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from packages import play_rps


# Init tkinter
rpy_apps = tk.Tk()
rpy_apps.configure(background='White')
rpy_apps.geometry('400x200')


# Varibale And Function
def userChoose(playerChoice):
    game_result = play_rps(playerChoice)
    showinfo(title='Result', message=game_result)


# Parent Container
container = ttk.Frame(rpy_apps)
container.pack(anchor='c', fill='both', expand=True)

# Header
header_rps = ttk.Label(container, text='Please Select one of them !')
header_rps.pack(expand=True, pady='5')

# Button Parent Container
container_button = tk.Frame(container)
container_button.pack(anchor='c', fill='x', expand=True)

# container_button.configure
button1_element = ttk.Button(
    container_button, text='Rock', command=lambda: userChoose(1))
button1_element.pack(side=tk.LEFT, padx=5, expand=True)

button2_element = ttk.Button(
    container_button, text='Paper', command=lambda: userChoose(2))
button2_element.pack(side=tk.LEFT, padx=5, expand=True)

button3_element = ttk.Button(
    container_button, text='Scissors', command=lambda: userChoose(3))
button3_element.pack(side=tk.LEFT, padx=5, expand=True)

rpy_apps.mainloop()
