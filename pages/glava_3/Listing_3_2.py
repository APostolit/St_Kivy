# Листинг 3.2
from kivy.app import App
from kivy.lang import Builder

KV = '''
AnchorLayout:
    anchor_x:'left'
    anchor_y: 'top'
    Button:
        text: 'Кнопка'
        size_hint: .3, .2
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()