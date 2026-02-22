# Листинг 12.6
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar, MDSnackbar

KV = '''
MDScreen:
    MDFloatingActionButton:
        x: root.width - self.width - dp(10)
        y: dp(10)
        icon: "android"
        on_release: app.snackbar_show()
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def snackbar_show(self):
        MDSnackbar(MDLabel(text="Сообщение в нижней панели")).open()

MainApp().run()