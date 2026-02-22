# Листинг 4.19
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

Window.clearcolor = '#19a8ffff'

class My_dd(App):
    def build(self):
        # Создать главную кнопку
        mainbutton = Button(text='Выпадающий список',
                            size_hint=(None, None),
                            pos_hint={'center_x': .5, 'center_y': .9},
                            size=(200, 50))
        # Создать выпадающий список
        dropdown = DropDown()
        # Добавить элементы в выпадающий список
        for index in range(5):
            btn = Button(text='Кнопка %d' % index,
                         size_hint_y=None,
                         height=44)
            btn.bind(on_release = lambda btn: (setattr(mainbutton,
                                                       'text', btn.text),
                                               dropdown.select(None)))
            dropdown.add_widget(btn)
        # Привязать главную кнопку к открытию выпадающего списка
        mainbutton.bind(on_release = dropdown.open)
        return mainbutton

My_dd().run()