# Листинг 2.55
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

class MainApp(App):
    def build(self):
        # Сетка окна приложения
        self.layout = GridLayout(cols=1, padding=30)
        self.l1 = Label(text='Главное окно', font_size=16)
        self.layout.add_widget(self.l1)  # Метка
        self.button = Button(text="Кнопка")
        self.layout.add_widget(self.button)   # Кнопка
        self.button.bind(on_press=self.onButtonPress)
        return self.layout

    # Обработка события нажатия кнопки приложения
    def onButtonPress(self, button):
        layout = GridLayout(cols=1, padding=10)
        self.popup = Popup(
            title='Окно диалога', content=layout,
            auto_dismiss=True, size_hint=(None, None),
            size=(200, 200))
        self.popup.open()
        popup_Label = Label(text="Модальное окно")
        layout.add_widget(popup_Label)  # Мета
        close_Button = Button(text="Закрыть")
        layout.add_widget(close_Button)  # Кнопка
        # Связать кнопку с событием
        close_Button.bind(on_press=self.on_close)

    # Обработка события нажатия кнопки диалогового окна
    def on_close(self, event):
        self.l1.text = 'Диалог закрыт'
        self.popup.dismiss()

MainApp().run()