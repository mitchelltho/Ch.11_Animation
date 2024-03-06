import arcade
import random


SW = 600

SH = 600


class Car_x:

    def __init__(self, pos_x, pos_y, width, height, col, dy, dx, tilt):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.width = width

        self.height = height

        self.col = col

        self.dy = dy

        self.dx = dx

        self.tilt = tilt

    def draw_Car_x(self):

        for i in range(3):
            arcade.draw_rectangle_filled(self.pos_x + (i * 350), self.pos_y, self.width, self.height, self.col, self.tilt)

    def update_Car_x(self):

        self.pos_y += self.dy

        self.pos_x += self.dx



        #Drive in a loop

        if self.pos_x == -100:

            self.pos_x = 700

        if self.pos_y == -100:

            self.pos_y = 700

class Car_y:

    def __init__(self, pos_x, pos_y, width, height, col, dy, dx, tilt):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.width = width

        self.height = height

        self.col = col

        self.dy = dy

        self.dx = dx

        self.tilt = tilt

    def draw_Car_y(self):

        for i in range(3):
            arcade.draw_rectangle_filled(self.pos_x, self.pos_y + (i * 350), self.width, self.height, self.col, self.tilt)

    def update_Car_y(self):

        self.pos_y += self.dy

        self.pos_x += self.dx



        #Drive in a loop

        if self.pos_x == -100:

            self.pos_x = 700

        if self.pos_y == -100:

            self.pos_y = 700

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.RED)


        self.Car_x = Car_x(100, 300, 50, 100, arcade.color.BLUEBERRY, 0, -5, 90)

        self.Car_y = Car_y(300, 700, 50, 100, arcade.color.BLUEBERRY, -5, 0, 0)

        self.clock = 3

    def on_draw(self):

        arcade.start_render()

        arcade.draw_rectangle_filled(300, 300, 900, 50, arcade.color.BLACK)
        arcade.draw_rectangle_filled(300, 300, 50, 900, arcade.color.BLACK)

        self.Car_x.draw_Car_x()

        self.Car_y.draw_Car_y()


    def on_update(self, dt):

        self.Car_x.update_Car_x()

        self.Car_y.update_Car_y()

        self.clock -= dt

        if 3 > self.clock > 2:
            arcade.set_background_color(arcade.color.RED)
        elif 2 > self.clock > 1:
            arcade.set_background_color(arcade.color.WHITE)
        elif 1 > self.clock > 0:
            arcade.set_background_color(arcade.color.BLUE)
        else:
            self.clock = 3
def main():

    window = MyGame(SW, SH, "UHS PARKING LOT!")

    arcade.run()



if __name__=="__main__":

    main()
