# Листинг 6.3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
import random
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class mywidget(Widget):
   def __init__(self, *args):
      super().__init__(*args)
      for i in range(100):
         colorR = random.randint(0, 255)
         colorG = random.randint(0, 255)
         colorB = random.randint(0, 255)
         posx = random.randint(0, Window.width)
         posy = random.randint(0, Window.height)
         self.canvas.add(Color(
            rgb=(colorR / 255.0, colorG / 255.0, colorB / 255.0)))
         d = 30
         self.canvas.add(Ellipse(pos=(posx, posy), size=(d, d)))

class Circlesapp(App):
   def build(self):
      w = mywidget()
      return w

Circlesapp().run()