# Листинг 5.9
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = '#19a8ffff'

class Scatterapp(App):
   def build(self):
      box=BoxLayout(orientation='vertical')
      scatr=Scatter()
      img=Image(source='images/Dog.jpg')
      scatr.add_widget(img)
      box.add_widget(scatr)
      return box

Scatterapp().run()