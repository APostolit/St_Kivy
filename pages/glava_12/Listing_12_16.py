# Листинг 12.16
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import MDSnackbar

KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "MDTopAppBar"
        left_action_items: [["menu", lambda x: app.callback()]]
    MDLabel:
        text: "Содержимое экрана"
        halign: "center"
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback(self):
        MDSnackbar(MDLabel(text="Нажата левая кнопка панели")).open()

MainApp().run()