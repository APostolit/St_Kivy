# Листинг 9.8
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp

KV = '''
MDScreen:          
    MDFlatButton:
        id: bt1
        text: "КНОПКА 1"        
        pos_hint: {"center_x": .5, "center_y": .6}
        on_press: app.bt_press(self.id)       
    MDFlatButton:
        id: bt2
        text: "КНОПКА 2"
        font_size: "30sp"
        font_name: 'Font/cataneo.ttf'
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        pos_hint: {"center_x": .5, "center_y": .4}
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