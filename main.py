from kivy.app import App                                            # Calling the App class from kivy app build
from kivy.uix.widget import Widget                                  # Calling the Widget class under UIX build
from kivy.properties import NumericProperty, ObjectProperty         # Adding Numeric and object property from property build
from kivy.vector import Vector                                      # Adding Vector
from kivy.clock import Clock                                        # Adding Clock for clock speed and velucity


class BricksMove(Widget):                                           # To move Brick object as ball receiver
    score = NumericProperty(0)                                      # Initialized to zero

    def BallBounce(self, ball):                                     # deffination for ball bouncing attitute
        if self.collide_widget(ball):
            vx, vy = ball.velocity                                  # Initialized the ball velucity in term of X & Y direction
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.2
            ball.velocity = vel.x, vel.y + offset

class BallObject(Widget):

    velocity_x = NumericProperty(0)                                     # velocity of the ball on x and y axis
    velocity_y = NumericProperty(0)


    def move(self):                                                     # Move function will move the ball one step. This
                                                                        #will be called in equal intervals to animate the ball
        self.pos = Vector(*self.velocity) + self.pos

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class GameWidget(Widget):                                              # Game widget for game play method
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):                                  # Auto update to serve from the centre
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):                                               # call ball.move and other stuff
        self.ball.move()

        self.player1.BallBounce(self.ball)                              # bounce of paddles
        self.player2.BallBounce(self.ball)

        if (self.ball.y < self.y) or (self.ball.top > self.top):        # bounce ball off bottom or top
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:                                        # went of to a side to score point?
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):                                     # Touch & Muse pointing behaviour
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):                                                     # App build by the KIVY defination
    def build(self):
        game = GameWidget()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 120.0)
        return game


if __name__ == '__main__':
    PongApp().run()                                                     # Build and Run the Pong Scorrer