# Листинг 2.42
from kivy.app import App
from kivy.lang import Builder

KV = '''
Widget:
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()