# Листинг 5.1
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Line
from kivy.uix.widget import Widget
Window.clearcolor = '#555555'

class drawLine(App):
   def build(self):
      widget = Widget()
      with widget.canvas:
         Line(rectangle=(50, 50, 200, 100),
              width=3)
         Line(rounded_rectangle=(50, 200, 250, 150,
                                 20, 20, 20, 20))
      return widget
drawLine().run()