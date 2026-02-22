# Листинг 4.20
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = '#19a8ffff'

class DropdownLabelExample(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Метка для показа результатов выбора
        self.lbl = Label(text='',
                         size_hint=(None, None),
                         pos_hint={'center_x': .5, 'center_y': .6})
        self.add_widget(self.lbl)

        # Кнопки с опциями выбора
        dropdown = DropDown()
        for val in ['Красный', 'Зеленый', 'Синий']:
            btn = Button(text=val, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn, v=val: dropdown.select(v))
            dropdown.add_widget(btn)
        dropdown.bind(on_select=lambda
            instance, x: setattr(self.lbl, 'text', f'Выбран: {x}'))

        # Главная кнопка выпадающего списка
        mainbtn = Button(text='Выбор цвета',
                         size_hint=(None, None),
                         width=120, height=40,
                         pos_hint={'center_x': .5, 'center_y': .5})
        mainbtn.bind(on_release=dropdown.open)
        self.add_widget(mainbtn)

class DropdownApp(App):
    def build(self):
        return DropdownLabelExample()

DropdownApp().run()