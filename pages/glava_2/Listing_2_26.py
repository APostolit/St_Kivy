# Листинг 2.26
from kivy.app import App
from kivy.lang import Builder

KV = '''
Image:
    source: "images/Dog.jpg"
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()