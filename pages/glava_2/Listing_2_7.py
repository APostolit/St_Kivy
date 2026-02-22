# Листинг 2.7
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        id: bt
        size_hint: (.5, .10)
        pos_hint: {'center_x': .5, 'center_y': .9}        
        text: 'Кнопка 1'        
        on_press: app.press_button(self.text)
        
    Label:
        id: label
        text: app.value
'''

class MainApp(App):
    def build(self):
        self.value = 'Приложение - MainApp'
        return Builder.load_string(KV)

    def press_button(self, instance):
        layout = GridLayout(cols=1, padding=10)
        close_Button = Button(text="Нажата " + instance)
        layout.add_widget(close_Button)
        self.popup = Popup(
            title='Диалоговое окно', content=layout,
            auto_dismiss=True, size_hint=(.8, .4),
        )
        self.popup.open()
        close_Button.bind(on_press=self.on_close)

    def on_close(self, event):
        self.popup.dismiss()
        MainApp().run()

MainApp().run()