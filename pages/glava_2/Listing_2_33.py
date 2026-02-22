# Листинг 2.33
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class MainApp(App):
    def build(self):
        t_but = ToggleButton(text="Кнопка",
                             font_size=20)
        return t_but

MainApp().run()