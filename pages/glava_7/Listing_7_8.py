# Листинг 7.8
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen

class MyApp(MDApp):
    def build(self):
        # Установить стиль темы 'Dark'
        self.theme_cls.theme_style = "Dark"
        # Установить основную палитру
        self.theme_cls.primary_palette = "Blue"
        # Установить акцентную палитру
        self.theme_cls.accent_palette = "Amber"
        screen = Screen ()
        button = MDRectangleFlatButton(
            text="Привет KivyMD",
            pos_hint={"center_x": 0.5, "center_y": 0.5 })
        screen.add_widget(button)
        return screen

MyApp().run( )