# Листинг 8.7
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDStackLayout:    
    orientation: "lr-tb"
    # orientation: "rl-bt"
    # orientation: "bt-lr"
    # orientation: "tb-rl"    
    md_bg_color: app.theme_cls.primary_color
    Button:
        text:"B1"
        font_size: 20
        size_hint: (.2, .1)
    Button:
        text:"B2"
        font_size: 20
        size_hint: (.2, .1)
    Button:
        text:"B3"
        font_size: 20
        size_hint: (.2, .1)
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()