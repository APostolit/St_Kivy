# Листинг 5.13
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import ColorProperty, NumericProperty
from kivy.core.window import Window

Window.clearcolor = '#19a8ffff'

class SliderExample(App):
   r = NumericProperty(0)
   g = NumericProperty(0)
   b = NumericProperty(0)
   t = NumericProperty(1)
   colour = ColorProperty([0, 0, 0, 1])

   def on_colour_change(self, instance, value):
      self.ttl.color = self.colour

   def on_red(self, instance, val):
      self.r = int(val) / 255
      self.colour = [self.r, self.g, self.b, self.t]
      self.redValue.text = str(int(val))

   def on_green(self, instance, val):
      self.g = int(val) / 255
      self.colour = [self.r, self.g, self.b, self.t]
      self.greenValue.text = str(int(val))

   def on_blue(self, instance, val):
      self.b = int(val) / 255
      self.colour = [self.r, self.g, self.b, self.t]
      self.blueValue.text = str(int(val))

   def build(self):
      maingrid = GridLayout(cols=1)
      self.ttl = Label(
         text='Выбранный цвет',
         color=self.colour, font_size=32
      )
      maingrid.add_widget(self.ttl)
      grid = GridLayout(cols=4)
      self.red = Slider(min=0, max=255)
      self.green = Slider(min=0, max=255)
      self.blue = Slider(min=0, max=255)

      grid.add_widget(Label(text='Красный'))
      grid.add_widget(self.red)
      grid.add_widget(Label(text='Значение слайдера'))
      self.redValue = Label(text='0')
      grid.add_widget(self.redValue)
      self.red.bind(value=self.on_red)

      grid.add_widget(Label(text='Зеленый'))
      grid.add_widget(self.green)
      grid.add_widget(Label(text='Значение слайдера'))
      self.greenValue = Label(text='0')
      grid.add_widget(self.greenValue)
      self.green.bind(value=self.on_green)

      grid.add_widget(Label(text='Синий'))
      grid.add_widget(self.blue)
      grid.add_widget(Label(text='Значение слайдера'))
      self.blueValue = Label(text='0')
      grid.add_widget(self.blueValue)
      self.blue.bind(value=self.on_blue)
      self.bind(colour=self.on_colour_change)
      maingrid.add_widget(grid)
      return maingrid

SliderExample().run()