# Листинг 2.25
from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        img = Image(source="images/Fon2.jpg")
        return img

MainApp().run()