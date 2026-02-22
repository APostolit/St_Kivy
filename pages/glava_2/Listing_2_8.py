# Листинг 2.8
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        id: bt
        size_hint: (.5, .10)
        pos_hint: {'center_x': .5, 'center_y': .9}  
        text: 'Кнопка 1'
        on_press: app.press_button(*args)
    TextInput:
        size_hint: (1, .5)
        pos_hint: {'center_x': .5, 'center_y': .5}       
        on_focus: self.insert_text("Фокус получен " if args[1] else "Фокус потерян ")
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def press_button(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(text=str(instance.text)),
                           size_hint=(.8, .4))
        self.popup.open()

MainApp().run()