import tkinter as tk

# Setup Settings - could be in another file ?
lives = 3
WIDTH = 600
HEIGHT = 480

# Setup Tk
main = tk.Tk()
frame = tk.Frame(main)
canvas = tk.Canvas(frame, width = WIDTH, height = HEIGHT, bg = '#AAAAFF')
frame.pack()
canvas.pack()

main.title('Main Window')
main.mainloop()