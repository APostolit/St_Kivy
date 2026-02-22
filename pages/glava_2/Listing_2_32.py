# Листинг 2.32
from kivy.app import App
from kivy.lang import Builder

KV = '''
TextInput:
    font_size: 30
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()