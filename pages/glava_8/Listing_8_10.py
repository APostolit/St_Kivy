# Листинг 8.10
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDCarousel:
    direction: 'right'
    loop: True
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

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()