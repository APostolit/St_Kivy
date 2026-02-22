# Листинг 2.51
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Basic_Class1(App):
    def build(self):
        button = Button(
            text='Кнопка',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return button

    def press_button(self):
        self.popup = Popup(
            title='Модальное окно',
            content=Label(text='Нажата кнопка'),
            size_hint=(.8, .4)
        )
        self.popup.open()
        print('Вы нажали на кнопку!')

My_App = Basic_Class1()
My_App.run()