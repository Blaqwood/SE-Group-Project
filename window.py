import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.resizable(0, 0)
        self.window.title("window") 
    def RickRoll():
        open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
root = Application()
btn = tk.Button(root, root.RickRoll())