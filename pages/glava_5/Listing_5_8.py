# Листинг 5.8
from kivy.app import App
from kivy.uix.rst import RstDocument
from kivy.uix.gridlayout import GridLayout

class Rstdemoapp(App):
   def build(self):
      grid=GridLayout(cols=1)
      doc = RstDocument(source="index.rst")
      grid.add_widget(doc)
      return grid
Rstdemoapp().run()