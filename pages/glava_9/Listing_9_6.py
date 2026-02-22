# Листинг 9.6
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDIconButton:
        pos_hint: {"center_x": .5, "center_y": .9}
    MDIconButton:
        id: bt             
        pos_hint: {"center_x": .5, "center_y": .8}        
        icon: "icon.png"
    MDIconButton:
        icon: "heart-outline"
        style: "standard"  
        pos_hint: {"center_x": .5, "center_y": .7} 
    MDIconButton:
        icon: "language-python"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .6}      
    
    MDIconButton:
        id: bt       
        icon: "language-python"        
        icon_size: "64sp"
        theme_text_color: "Custom"
        icon_color: "green"       
        pos_hint: {"center_x": .5, "center_y": .4}
        on_press: app.bt_press(self.id)
                
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def bt_press(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(text='Нажата иконка'),
                           size_hint=(.8, .4))
        self.popup.open()

MainApp().run()