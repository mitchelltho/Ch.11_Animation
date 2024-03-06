'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''

import arcade
import random


SW = 600

SH = 900


class Player:

    def __init__(self, pos_x, pos_y, rad, col, dx):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.rad = rad

        self.col = col

        self.dx = dx

    def draw_Player(self):

        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_Player(self):

        if input == "a":

            self.dx = -3

        if input == "d":

            self.dx = 3

class SubCar:

    def __init__(self, pos_x, pos_y, width, height, col, dy, dx, tilt):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.width = width

        self.height = height

        self.col = col

        self.dy = dy

        self.dx = dx

        self.tilt = tilt

    def draw_SubCar(self):

        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col, self.tilt)

    def update_SubCar(self):

        self.pos_y += self.dy

        self.pos_x += self.dx

        #Loop SubCars

        if self.pos_y == -150:

            self.pos_y = random.randint(1000,1600)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.GREEN)

        self.Player = Player(300, 150, 50, arcade.color.RED, 0)

        self.SubCar = SubCar(100, random.randint(1000, 1600), 200, 500, arcade.color.ORANGE, -5, 0, 0)

        self.clock = 5

    def on_draw(self):

        arcade.start_render()

        self.SubCar.draw_SubCar()

        self.Player.draw_Player()

    def on_update(self, dt):

        self.SubCar.update_SubCar()

        self.Player.update_Player()

        self.clock -= dt

        if self.clock <= 0:



            self.clock = 5

def main():

    window = MyGame(SW, SH, "Maybe soon to be functional game!")

    arcade.run()



if __name__=="__main__":

    main()
