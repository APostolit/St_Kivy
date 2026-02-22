# Листинг 2.20
from kivy.app import App
from kivy.lang import Builder

KV = '''
Label:
    text: "Текст метки из KV"
    font_size: 20  
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()