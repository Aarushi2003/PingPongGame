from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import sys
import PongBall
import Player
from UserNamesInputForm import UserNamesInputForm
from kivy.lang import Builder
from kivy.graphics import Rectangle

class SplashScreen(Widget):
    def dummy():
        return

#PongGame is graphical widget, which is enhanced with our specific functions
# This looks for similar name in any of the kivy files, to initialize it's layout
# >>>>> Didn't understand, how come widget is appearing without any parent layout. Is Widget a layout?
# 
class PongGame(Widget):
    MAX_SCORE = 2
    flag_game_initialised = False
    pong_ball = ObjectProperty(None)
    winning_player = None
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player1_score = ObjectProperty(None)
    player2_score = ObjectProperty(None)
    player1_score_value = 0
    player1_name = ObjectProperty(None)
    player2_name = ObjectProperty(None)
    player2_score_value = 0
    player_names_entered = False
    winning_splash = ObjectProperty(None)
    winning_splash_object = ObjectProperty(None)
    p1_name = "Paridhi"
    p2_name = "Aarushi"
    unInputForm = ObjectProperty(None)
    splash_screen = ObjectProperty(None)

    timer_running = False
    timer = None

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.winning_splash_object = self.winning_splash.__self__
        self.clear_widgets(children = [self.player1_score, self.player2_score, self.player1_name, self.player2_name, self.player1, self.player2, self.winning_splash])
        self.splash_timer = Clock.schedule_once(self.remove_splash, 3)

    def paintBoard(self):
        with self.canvas:
            Rectangle(source='mylogo.png', pos=(self.center_x - 5, 0), size=(10, self.height))
        return

    def remove_splash(self, dt):
        self.clear_widgets(children = [self.splash_screen])
        self.paintBoard()

#        self.add_widget(self.pong_ball)
        self.add_widget(self.player1_score)
        self.add_widget(self.player1_name)
        self.add_widget(self.player2_score)
        self.add_widget(self.player2_name)
        self.add_widget(self.player1)
        self.add_widget(self.player2)
        self.flag_game_initialised = True
        self.askPlayerNames()

    def names_received(self, caller, names):
        print("Names received", names)
#        self.paintBoard()
        self.player1_name.text = names[0]
        self.player2_name.text = names[1]
        self.clear_widgets(children=[self.unInputForm])
        self.player_names_entered = True

        #TODO ideally this should not be re-installed
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)    
        return

    def names_not_received(self):
        #TODO - Throw a error box
        print("Names not received")

    def showWinningTeam(self):
        self.winning_splash.text = self.winning_player + " Won"
        self.add_widget(self.winning_splash)

    def askPlayerNames(self):
        self.unInputForm = UserNamesInputForm(self, self.names_received, self.names_not_received)
        self.add_widget(self.unInputForm)
        return

    def resetGam(self):
        return

    def update(self, dt):
        # call ball.move and other stuff
        self.pong_ball.move()
        # Check if ball has touched the player 1
        if(not (self.pong_ball.center_y < self.player1.top and self.pong_ball.center_y > self.player1.y) and self.pong_ball.x < 0):
            self.player2_score_value += 1
            self.player2_score.text = str(self.player2_score_value)
            if(self.player2_score_value >= self.MAX_SCORE):
                self.winning_player = self.player2_name.text
            self.timer.cancel()
            self.timer_running = False
            self.serve_ball()

       # Check if pong_ball has touched the player 2
        if(not (self.pong_ball.center_y < self.player2.top and self.pong_ball.center_y > self.player2.y) and self.pong_ball.right > self.width):
            self.player1_score_value += 1
            self.player1_score.text = str(self.player1_score_value)
            if(self.player1_score_value >= self.MAX_SCORE):
                self.winning_player = self.player1_name.text
            self.timer.cancel()
            self.timer_running = False
            self.serve_ball()

        if(self.winning_player != None):
            print("Game won by", self.winning_player)
            self.showWinningTeam()
    
        # bounce off top and bottom
        if (self.pong_ball.y < 0) or (self.pong_ball.top > self.height):
            self.pong_ball.velocity_y *= -1

        # bounce off left and right
        if (self.pong_ball.x < 0) or (self.pong_ball.right > self.width):
            self.pong_ball.velocity_x *= -1
    # ``move`` function will move the pong_ball one step. This
    #  will be called in equal intervals to animate the pong_ball
        return True


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def invokeUserNamesInput(self):
            if(self.flag_game_initialised):
                if(self.timer_running == False and self.player_names_entered == False):
                    self.askPlayerNames()
                elif(self.timer_running == False and self.winning_player == None):
                    self.timer = Clock.schedule_interval(self.update, 1.0/60.0)
                    self.timer_running = True


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print("Flags are: ", self.timer_running, self.player_names_entered, self.winning_player, self.flag_game_initialised)
        if keycode[1] == 'w':
            self.player1.center_y += 20
            if(self.player1.top > self.height):
                self.player1.top -= 20
        elif keycode[1] == 's':
            self.player1.center_y -= 20
            if(self.player1.y < 0):
                self.player1.y += 20
        elif keycode[1] == 'up':
            self.player2.center_y += 20
            if(self.player2.top > self.height):
                self.player2.top -= 20
        elif keycode[1] == 'down':
            self.player2.center_y -= 20
            if(self.player2.y < 0):
                self.player2.y += 20
        elif keycode[1] == 'q' or keycode[1] == 'Q':
            sys.exit()
        else:
            self.invokeUserNamesInput()

    def serve_ball(self):
        self.pong_ball.center = self.center
        angle = randint(0, 360-120)
        print("Random integer: ", angle)
        if(angle > 60):
            angle+=60
        if(angle > 240):
            angle+=60
        self.pong_ball.velocity = Vector(6, 0).rotate(angle)
        self.player1.center = Vector(0,350)
        self.player2.center = Vector(800,300)
        print("Serve", self.center[0], self.center[1], angle)
 

class PongApp(App):
    def load_kivy_files(self):
        Builder.load_file('usernames.kv')
#        Builder.load_file('pong2.kv')

#Note that build has to return a layout, which in this case is a widget. This can be boxlayout, relative layout etc
    def build(self):
        self.load_kivy_files()
        game = PongGame()
        game.serve_ball()
#        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()