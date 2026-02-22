# Листинг 2.19
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        L = Label(text="Это текст метки", font_size=20)
        return L

MainApp().run()