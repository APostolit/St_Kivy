# Листинг 9.14
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDFillRoundFlatButton:
        text: "Кнопка 1"        
        pos_hint: {"center_x": .5, "center_y": .7}
        on_press: app.bt_press(self.id)
    MDFillRoundFlatButton:
        text: "Кнопка 2"
        font_size: "25sp"        
        pos_hint: {"center_x": .5, "center_y": .5}
        on_press: app.bt_press(self.id) 
    MDFillRoundFlatButton:
        text: "Кнопка 3"
        font_size: "25sp"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        md_bg_color: 0, 1, 0, 1
        pos_hint: {"center_x": .5, "center_y": .3}
        on_press: app.bt_press(self.id) 
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def bt_press(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(text='Нажата кнопка'
                                              + instance),
                           size_hint=(.8, .4))
        self.popup.open()

MainApp().run()
