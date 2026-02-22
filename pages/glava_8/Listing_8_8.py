# Листинг 8.8
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDStackLayout:
    padding: "20dp"
    spacing: "10dp"  
    orientation: "lr-tb"       
    md_bg_color: app.theme_cls.primary_color
    MDFlatButton:
        text:"Кнопка 1"
        md_bg_color: 0.8, 0.8, 0.8, 1
        font_size: 14
        size_hint: (.15, .08)
    MDFlatButton:
        text:"Кнопка 2"
        md_bg_color: 0.8, 0.8, 0.8, 1
        font_size: 14
        size_hint: (.15, .08)
    MDFlatButton:
        text:"Кнопка 3"
        md_bg_color: 0.8, 0.8, 0.8, 1
        font_size: 14
        size_hint: (.15, .08)
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()