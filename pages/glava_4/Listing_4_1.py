# Листинг 4.1
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.accordion import Accordion, AccordionItem

class MainApp(App):
    def build(self):
        # Виджет Аккордеон
        acc = Accordion(orientation='horizontal')
        # Элемент 1 аккордеона
        item1 = AccordionItem(title='Панель с текстом')
        item1.add_widget(Label(text='Привет Аккордеон'))

        # Элемент 2 аккордеона
        item2 = AccordionItem(title='Панель с кнопкой')
        btn = Button(text='Кнопка')
        item2.add_widget(btn)

        # Элемент 3 аккордеона
        item3 = AccordionItem(title='Панель с изображением')
        img = Image(source='images/Elena.jpg')
        item3.add_widget(img)

        # Загрузить элементы в аккордеон
        acc.add_widget(item1)
        acc.add_widget(item2)
        acc.add_widget(item3)
        return acc

MainApp().run()