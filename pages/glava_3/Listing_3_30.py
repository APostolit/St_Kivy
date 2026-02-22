# Листинг 3.30
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        # создать объект
        carousel = Carousel(direction='right')

        img = Image(source='images/Angelika.jpg')
        carousel.add_widget(img)

        img = Image(source='images/Elena.jpg')
        carousel.add_widget(img)

        img = Image(source='images/Flora.jpg')
        carousel.add_widget(img)

        img = Image(source='images/Fortuna.jpg')
        carousel.add_widget(img)

        return carousel

MainApp().run()