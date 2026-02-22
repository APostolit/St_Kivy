# Листинг 4.28
from kivy.lang import Builder
from kivy.app import App

KV = '''
Carousel:
    direction: 'right'
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        Image:
            source: "images/Margaritta.jpg"
    BoxLayout:
        Image:
            source: "images/Marinara.jpg"    
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()