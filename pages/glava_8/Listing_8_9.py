# Листинг 8.9
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.carousel import MDCarousel

class MainApp(MDApp):
    def build(self):
        # создать объект
        carousel = MDCarousel(direction='right')
        img = Image(source='images/Gorox.jpg')
        carousel.add_widget(img)
        img = Image(source='images/Ganna.jpg')
        carousel.add_widget(img)
        img = Image(source='images/Flora.jpg')
        carousel.add_widget(img)
        img = Image(source='images/Victoria.jpg')
        carousel.add_widget(img)
        return carousel

MainApp().run()