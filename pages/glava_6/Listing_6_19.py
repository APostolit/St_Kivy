# Листинг 6_19
from kivy.lang import Builder
from kivy.app import App

KV = '''
Carousel:
    direction: 'right'
    canvas:
        Rectangle:
            source: 'images/Fon.jpg'
            pos: self.pos
            size: self.size   
    BoxLayout:
        Image:
            source: "images/Montanara.jpg"

    BoxLayout:
        Image:
            source: "images/Napoletana.jpg"  
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()