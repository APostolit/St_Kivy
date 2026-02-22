# Листинг 12.14
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: "vertical"
    MDTextField:
        hint_text: "Введите текст"
        width: 300
        size_hint_x: None
        pos_hint: {"center_x":.5}
        mode: 'round'
    MDTextField:
        hint_text: "Поле с иконкой слева"
        icon_left: "email"
        width: 300
        size_hint_x: None
        pos_hint: {"center_x":.5}
        mode: 'round'
    MDTextField:
        hint_text: "Поле с иконкой справа"
        # icon_left: 'email'
        icon_right: 'eye-off'
        width: 300
        size_hint_x: None
        pos_hint: {"center_x":.5}
        mode: 'round'                
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()