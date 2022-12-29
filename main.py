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

        # Implementing the objects on canvas frame
        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle

        for z in range(5, self.width - 5, 75):
            self.add_brick(z + 37.5, 50, 2)
            self.add_brick(z + 37.5, 70, 1)
            self.add_brick(z + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind('<Left>', lambda _: self.paddle.move(-10))
        self.canvas.bind('<Right>', lambda _: self.paddle.move(10))

    def setup_game(self):
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, 'Press <SPACE> to start')
        self.canvas.bind('<space>', lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        pos_x = (paddle_coords[0] + paddle_coords[2] * 0.1)
        self.ball = Ball(self.canvas, pos_x, 310)
        self.paddle.setball(self.ball)

    def add_brick(self, pos_x, pos_y, hits):
        brick = Brick(self.canvas, pos_x, pos_y, hits)
        self.items[brick.item] = brick

    def draw_text(self, pos_x, pos_y, text, size = '40'):
        font = ('Helvetica', size)
        return self.canvas.create_text(pos_x, pos_y, text = text, font = font)

    def update_lives_text(self):
        text = 'Lives : %s' % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text = text)

    def start_game(self):
        pass

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
        item = canvas.create_rectangle(pos_x - self.width / 2, pos_y - self.height / 2, pos_x + self.width / 2, pos_y + self.height / 2, fill = 'blue')
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

class Brick(GameObject):
    COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}
    def __init__(self, canvas, pos_x, pos_y, hits):
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(pos_x - self.width / 2, pos_y - self.height / 2, pos_x + self.width / 2, pos_y + self.height / 2, fill = color, tags = 'bricks')
        super(Brick, self).__init__(canvas, item)

    def got_hit(self):
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item, fill = Brick.COLORS[self.hits])

if __name__ == '__main__':
    main = tk.Tk()
    main.title('Breakout_Py')
    game = Game(main)

    # item = game.canvas.create_rectangle(10, 10, 100, 80, fill='green') # paddle
    # game_object = GameObject(game.canvas, item)
    
    game.mainloop()
