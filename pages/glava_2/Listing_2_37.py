# Листинг 2.37
from kivy.app import App
from kivy.lang import Builder

KV = '''
Switch:
    active: True
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()