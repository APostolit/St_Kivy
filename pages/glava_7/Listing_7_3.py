# Листинг 7.3
from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
Screen:
    MDTopAppBar:
        title: "Приложение KivyMD"
        elevation: 3
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [["menu", lambda x: x]]
        pos_hint: {"top": 1}

    MDRaisedButton:
        text: "Кнопка KivyMD"
        pos_hint: {"center_x": .5, "center_y": .5}
"""

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()