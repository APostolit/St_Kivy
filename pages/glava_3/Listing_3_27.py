# Листинг 3.27
from kivy.app import App
from kivy.lang import Builder

KV = '''
StencilView:
    Scatter:
        Image:
            source: "images/Dog.jpg"
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
