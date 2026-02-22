# Листинг 4.14
from kivy.lang import Builder
from kivy.app import App

KV = '''
Carousel:
    direction: 'bottom'
    BoxLayout:
        Image:
            source: "images/Margaritta.jpg"
    BoxLayout:
        Image:
            source: "images/Marinara.jpg"
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