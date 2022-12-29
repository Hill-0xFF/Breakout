import tkinter as tk
from settings import WIDTH, HEIGHT

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = WIDTH
        self.height = HEIGHT
        self.canvas = tk.Canvas(self, bg="#AAAAFF", width = self.width, height = self.height)

        self.canvas.pack()
        self.pack()

if __name__ == '__main__':
    main = tk.Tk()
    main.title('Breakout_Py')
    game = Game(main)
    game.mainloop()