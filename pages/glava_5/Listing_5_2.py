# Листинг 5.2
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

KV = '''
Widget:
    canvas:
        Line:
            rectangle: (50, 50, 200, 100)
            width: 3
        Color:
            rgb: (1,0,0,1)
        Line:
            ellipse: (50, 70, 200, 200)
            width: 4  
'''
Window.clearcolor = '#19a8ffff'

class Wline(App):
    def build(self):
        return Builder.load_string(KV)

Wline().run()
