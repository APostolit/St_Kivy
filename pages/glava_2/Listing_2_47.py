# Листинг 2.47
from kivy.app import App
from kivy.lang import Builder

KV = '''
Button:
    text: 'Кнопка'
    size_hint: None, None
    size: 100, 35
    pos: 10, 10
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()