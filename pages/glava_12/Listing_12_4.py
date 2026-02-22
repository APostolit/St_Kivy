# Листинг 12.4
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import MDSnackbar

KV = '''
MDScreen:
    MDRaisedButton:
        text: "Открыть Snackbar"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.press(self.text)       
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def press(self, instance):
        MDSnackbar(MDLabel(text="Сообщение в нижней панели")).open()

MainApp().run()