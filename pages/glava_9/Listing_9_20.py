# Листинг 9.20
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "MDTopAppBar"

    MDLabel:
        text: "Метка в окне приложения"
        halign: "center"
    
    MDChip:        
        on_release: app.on_release_chip(self)
        MDChipText:
            text: "Простой MDChip"
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_release_chip(self, instance_check):
        popup = Popup(title='Модальное окно',
                      content=Label(text='Выбран MDChip'),
                      size_hint=(.8, .4))
        popup.open()

MainApp().run()