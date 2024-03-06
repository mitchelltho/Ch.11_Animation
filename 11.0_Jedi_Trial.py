import arcade



SW = 600

SH = 600



class Clock:

    def __init__(self,time):

        self.time = time

    def draw_Clock(self):

        self.time = 0

    def update_Clock(self):

        self.time += 0.01666666666

class Electron:

    def __init__(self, pos_x, pos_y, dx, dy, rad, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.dx = dx

        self.dy = dy

        self.rad = rad

        self.col = col

    def draw_Electron(self):

        for i in range(50):
            arcade.draw_circle_filled(self.pos_x + (i * 50), self.pos_y, self.rad, self.col)

    def update_Electron(self):

        self.pos_y += self.dy

        self.pos_x += self.dx



        #Move around the circuit

        if self.pos_x < self.rad:

            self.dx = 0
            self.dy = 5

        if self.pos_x > SW - self.rad:

            self.dx = 0
            self.dy = -5

        if self.pos_y < self.rad:

            self.dy = 0
            self.dx = -5

        if self.pos_y > SH - self.rad:

            self.dy = 0
            self.dx = 5

class Light:

    def __init__(self, pos_x, pos_y, width, height, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.width = width

        self.height = height

        self.col = col

    def draw_Light(self):

        arcade.draw_rectangle_filled(300, 300, 500, 500, arcade.color.BLACK)

    def update_Light(self):

        self.col = arcade.color.LIGHT_YELLOW

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ANTIQUE_BRASS)


        self.Electron = Electron(700, 25, -5, 0, 25, arcade.color.COPPER)
        self.Light = Light(300, 300, 500, 500, arcade.color.BLACK)
        self.Clock = Clock(time=0)

    def on_draw(self):

        arcade.start_render()

        self.Electron.draw_Electron()

        self.Light.draw_Light()

        self.Clock.draw_Clock()

    def on_update(self, dt):

        self.Electron.update_Electron()

        self.Light.update_Light()

        self.Clock.update_Clock()

def main():

    window = MyGame(SW, SH, "Electricity!")

    arcade.run()



if __name__=="__main__":

    main()