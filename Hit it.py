from turtle import *
from time import sleep

class Sprite(Turtle):
    def __init__(self, x, y, step = 10, shape = 'circle', color = 'black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False
    def set_move (self, x_start, y_start, x_end, y_end,):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto (x_start, y_start)
        self.setheading(self.towards (x_end, y_end))
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

Player = Sprite(0, -100, 10, 'circle', 'orange')
Enemy1 = Sprite(-150, 85, 10, 'square', 'red')
Enemy1.set_move(-150, 85, 150, 85)
Enemy2 = Sprite(150, 130, 10, 'square', 'red')
Enemy2.set_move(150, 130, -150, 130)
Enemy3 = Sprite(110, 50, 10, 'turtle', 'medium purple')
Enemy3.set_move(110, 50, -110, 50)
Target = Sprite(0, 200, 10, 'triangle', 'green')
scr = Player.getscreen()
scr.listen()

scr.onkey(Player.move_up, 'Up')
scr.onkey(Player.move_right, 'Right')
scr.onkey(Player.move_left, 'Left')
scr.onkey(Player.move_down, 'Down')
total_score = 0
while total_score < 3:
    Enemy1.make_step()
    Enemy2.make_step()
    Enemy3.make_step()
    if Player.is_collide(Target):
        Player.goto(0, -100)
        total_score += 1
    if total_score == 3:
        Player.write('YOU WIN!', font=('Arial', 25, 'bold'))
    if Player.is_collide(Enemy1) or Player.is_collide(Enemy2) or Player.is_collide(Enemy3):
        Player.write('YOU LOSE! >:)', font=('Arial', 25, 'bold'))
        Target.hideturtle()
        break
Enemy1.hideturtle()
Enemy2.hideturtle()
Enemy3.hideturtle()
done()