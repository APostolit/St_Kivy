# Листинг 4.13
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        # создать объект - карусель
        carousel = Carousel(direction='right')
        # Добавить слайды с изображениями
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