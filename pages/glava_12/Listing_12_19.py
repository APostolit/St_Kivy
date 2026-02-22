# Листинг 12.19
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import MDSnackbar

KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "MDTopAppBar"
        md_bg_color: app.theme_cls.accent_color
        specific_text_color: 0,0,1,1
        elevation: 2
        left_action_items: [["menu", lambda x: app.callback_l()]]
        right_action_items: [["dots-vertical", lambda x: app.callback_r()]]
    MDLabel:
        text: "Содержимое экрана"
        halign: "center"
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def callback_l(self):
        MDSnackbar(MDLabel(text="Нажата левая кнопка панели")).open()
    def callback_r(self):
        MDSnackbar(MDLabel(text="Нажата правая кнопка панели")).open()

MainApp().run()