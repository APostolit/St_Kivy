# Листинг 9.18
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "480dp", "280dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: .8, .8, .8, 1
        MDLabel:
            text: "Заголовок"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]
        MDSeparator:
            height: "1dp"
        Image:
            source: 'images/Dog.jpg'            
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
