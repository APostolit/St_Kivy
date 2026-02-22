# Листинг 2.21
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        btn = Button(text="Это кнопка", font_size=20)
        return btn

MainApp().run()