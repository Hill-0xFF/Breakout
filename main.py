import tkinter as tk
from settings import WIDTH, HEIGHT

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives: int = 3
        self.width: int = WIDTH
        self.height: int = HEIGHT
        self.canvas = tk.Canvas(self, bg="#AAAAFF", width = self.width, height = self.height)

        self.canvas.pack()
        self.pack()

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item
    
    def get_position(self):
        return self.canvas.coords(self.item)
    
    def move(self, pos_x, pos_y):
        self.canvas.move(self.item, pos_x, pos_y)

    def delete(self):
        self.canvas.delete(self.item)

if __name__ == '__main__':
    main = tk.Tk()
    main.title('Breakout_Py')
    game = Game(main)
    game.mainloop()
