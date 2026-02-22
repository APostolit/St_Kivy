# Листинг 9.7
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDFloatingActionButton:
        id: bt
        icon: 'microphone'
        elevation: 2
        pos_hint: {"center_x": .5, "center_y": .5}        
        on_release: app.bt_release(self.id)    
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def bt_release(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(text='Кнопка отпущена'),
                           size_hint=(.8, .4))
        self.popup.open()

MainApp().run()