from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class PopupExample(App):
    def build(self):
        self.layout = GridLayout(cols=1, padding=10)
        # Метка окна приложения
        self.l1 = Label(text='Метка окна приложения')
        self.layout.add_widget(self.l1)
        # Кнопка окна приложения
        self.button = Button(text="Открыть окно",
                             size_hint=(None, None),
                             size=(150, 50))
        self.layout.add_widget(self.button)
        self.button.bind(on_press=self.onButtonPress)
        return self.layout

    # Обработка события нажатия кнопки приложения
    def onButtonPress(self, button):
        layout = GridLayout(cols=1, padding=10)
        # Метка всплывающего окна
        popupLabel = Label(text="Введите текст")
        # Поле для ввода текста всплывающего окна
        self.t1 = TextInput()
        # Кнопка всплывающего окна
        closeButton = Button(text="Закрыть окно")
        closeButton.bind(on_press=self.on_close)

        layout.add_widget(popupLabel)
        layout.add_widget(self.t1)
        layout.add_widget(closeButton)
        # Всплывающее окно
        self.popup = Popup(
            title='Заголовок', content=layout,
            auto_dismiss=False, size_hint=(None, None),
            size=(200, 200))
        self.popup.open()

    # Обработка события кнопки закрытия диалогового окна
    def on_close(self, event):
        self.l1.text = 'Введено: ' + self.t1.text
        self.popup.dismiss()

PopupExample().run()