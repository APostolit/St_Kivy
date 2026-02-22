# Листинг 2.50
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup

KV = '''
Button:
    text: 'Кнопка'
    size_hint: .5, .5
    pos_hint: {'center_x': .5, 'center_y': .5}
    on_press: app.press_button(root)
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def press_button(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(
                               text= 'Нажата ' + str(instance.text)),
                           size_hint=(.8, .4))
        self.popup.open()

MainApp().run()