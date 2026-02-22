# Листинг 3.18
from kivy.app import App
from kivy.lang import Builder

KV = '''
RelativeLayout:
    Scatter:
        Image:
            source: "images/forest.jpg"
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()