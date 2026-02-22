# Листинг 6.20
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    Button:
        id: but
        text: "КНОПКА"        
    TextInput:
        id: txt
        text: but.state
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()