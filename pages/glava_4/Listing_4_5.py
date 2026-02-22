# Листинг 4.5
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.bubble import Bubble, BubbleContent
from kivy.uix.bubble import BubbleButton
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

class BubbleApp(App):
    def build(self):
        Window.clearcolor = '#19a8ffff'
        self.root = FloatLayout()
        # создать кнопку с залипанием
        self.button = ToggleButton(text='Показать меню',
                        size_hint=(None, None),
                        size=(200, 75),
                        pos_hint={'center_x': .5, 'center_y': .45},
                        on_press=self.show_bubble)
        # Добавить кнопку к окну приложения
        self.root.add_widget(self.button)

        self.lab = Label(text='',
                        size_hint=(None, None),
                        size=(200, 75),
                        pos_hint={'center_x': .5, 'center_y': .15},)
        # Добавить кнопку к окну приложения
        self.root.add_widget(self.lab)
        return self.root

    # Функция обработки кнопки с залипанием
    def show_bubble(self, instance):
        if instance.text == 'Показать меню':
            # Создать раскрывающееся меню bubble
            bubble = Bubble(size_hint=(None, None),
                            size=(200, 50),
                            pos_hint={'center_x': .5, 'y': .5})
            # Создать контент меню
            bub_con = BubbleContent()
            # Создать кнопки в контенте меню
            button1 = BubbleButton(text = "Меню 1")
            button1.bind(on_press=self.press_btn)
            bub_con.add_widget(button1)

            button2 = BubbleButton(text = "Меню 2")
            button2.bind(on_press=self.press_btn)
            bub_con.add_widget(button2)

            button3 = BubbleButton(text = "Меню 3")
            button3.bind(on_press=self.press_btn)
            bub_con.add_widget(button3)
            bubble.add_widget(bub_con)
            self.root.add_widget(bubble)
            self.button.text = 'Скрыть меню'
        else:
            self.button.text = 'Показать меню'
            # Очистить окно приложения
            self.root.clear_widgets()
            # Вернуть кнопку с залипанием
            self.button = ToggleButton(text='Показать меню',
                                       size_hint=(None, None),
                                       size=(200, 75),
                                       pos_hint={'center_x': .5,
                                                 'center_y': .45},
                                       on_press=self.show_bubble)
            self.root.add_widget(self.button)
            self.lab = Label(text='',
                             size_hint=(None, None),
                             size=(200, 75),
                             pos_hint={'center_x': .5,
                                       'center_y': .15}, )
            self.root.add_widget(self.lab)

    # Create the BubbleApp class
    def press_btn(self, value):
        self.lab.text = value.text

BubbleApp().run()