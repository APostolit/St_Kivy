# Листинг 9.1
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDScreen:
    MDBackdrop:  # общие параметры backdrop
        id: backdrop
        header: True
        title: "Заголовок заднего слоя"
        header_text: 'Заголовок переднего слоя'
        right_action_items: [['login',lambda x: print("Кнопка Вход")],
                            ['apple', lambda x: print("Кнопка Apple")]]
        #padding: [20]  # Отступ подзаголовка от верхнего края
        #radius_right: "0dp"
        #radius_left: "0dp"
        #close_icon: 'account'          
                
        # параметры элементов заднего слоя
        MDBackdropBackLayer:
            MDRoundFlatButton:
                text: 'Кнопка заднего слоя'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                md_bg_color: 0, 1, 0, 1 
                pos_hint: {"center_x":.5,"center_y":.20}
                on_press: app.callback1(*args)
            MDLabel:
                id: lb_back
                text: "Метка заднего слоя"                 
                theme_text_color: "Custom"
                text_color: 1, 1, 0, 1        
        # параметры элементов переднего слоя
        MDBackdropFrontLayer:
            MDRoundFlatButton:                    
                text: 'Кнопка переднего слоя'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                md_bg_color: 0, 1, 0, 1  
                on_press: app.callback2(*args)
            MDLabel:
                id: lb_front
                text: "Метка переднего слоя"               
                theme_text_color: "Custom"
                text_color: 0, 0, 1, 1                  
"""

class Myapp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback1(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(text=str(instance.text)),
                           size_hint=(.8, .4))
        self.popup.open()

    def callback2(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(text=str(instance.text)),
                           size_hint=(.8, .4))
        self.popup.open()

Myapp().run()