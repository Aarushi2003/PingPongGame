from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector

class PongBall(Widget):

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    print("Initial Position: ", velocity_x, velocity_y)
 
    def move(self):
#        print("Before...", self.pos[0], self.pos[1])
        self.pos = Vector(*self.velocity) + self.pos
#        print("After...", self.pos[0], self.pos[1])
