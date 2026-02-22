# Листинг 10.6
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    padding: 15
    Image:
        source: "images/forest.jpg"
        size: self.texture_size
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()