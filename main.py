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

class Ball(GameObject):
    def __init__(self, canvas, pos_x, pos_y):
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_oval(pos_x - self.radius, pos_y - self.radius, pos_x + self.radius, pos_y + self.radius, fill = 'white' )
        super(Ball, self).__init__(canvas, item)

class Paddle(GameObject):
    def __init__(self, canvas, pos_x, pos_y):
        self.width = 80
        self.height = 10
        self.ball = None
        item = canvas.create_rectangle(pos_x - self.width / 2, pos_y - self.width / 2, pos_x + self.width / 2, pos_y + self.width / 2, fill = 'blue')
        super(Paddle, self).__init__(canvas, item)

    def setball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo_width()

        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset)

            if self.ball is not None:
                self.ball.move(offset, 0)

if __name__ == '__main__':
    main = tk.Tk()
    main.title('Breakout_Py')
    game = Game(main)

    item = game.canvas.create_rectangle(10, 10, 100, 80, fill='green') # paddle
    game_object = GameObject(game.canvas, item)
    
    game.mainloop()
