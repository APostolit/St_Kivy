# Листинг 4.17
from kivy.app import App
from pygments.lexers.python import Python3Lexer
from kivy.uix.scrollview import ScrollView
from kivy.uix.codeinput import CodeInput
from kivy.core.window import Window

class CodeinputApp(App):
   def build(self):
      scr = ScrollView(size=Window.size)
      codinp = CodeInput(style='emacs',
                         size_hint_y=None,
                         )
      codinp.height = max(codinp.minimum_height, 2000)
      file=open('Listing_4_16.py')
      text=file.read()
      codinp.text=text
      scr.add_widget(codinp)
      return scr

CodeinputApp().run()