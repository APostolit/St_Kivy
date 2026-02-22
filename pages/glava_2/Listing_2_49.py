# Листинг 2.49
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.button = Button(text='Кнопка',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        self.button.bind(on_press=self.press_button)
        return self.button

    def press_button(self, instance):
        self.button.text = 'Кнопка нажата'

MainApp().run()
