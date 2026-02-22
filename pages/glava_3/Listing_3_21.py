# Листинг 3.21
from kivy.app import App
from kivy.lang import Builder

KV = '''
RelativeLayout:
    canvas:
        Rectangle:
            source: 'images/Fon.jpg'
            size: self.size
            pos: self.pos

    ScatterLayout:
        Image:
            source: "images/forest.jpg"

'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()