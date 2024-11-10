
from tkinter import * 

Bg_color = "Red"

def start():
    window = Tk()
    window.title('Test')

    canvas = Canvas(window, bg = Bg_color, width = 600, height = 800)
    canvas.pack()

if __name__ == '__main__':
    start()