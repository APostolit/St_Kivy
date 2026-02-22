# Листинг 12.15
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "Панель MDTopAppBar"
    MDLabel:
        text: "Содержимое экрана"
        halign: "center"
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()