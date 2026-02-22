# Листинг 11.13
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

KV = '''
MDScreen:
    MDGridLayout:
        cols:2
        spacing: 2

        MDLabel:
            size_hint_x: None
            text: ' Флажок 1'
        MDCheckbox:            
            size_hint_x: None
            size_hint_x: None
            size: "48dp", "48dp"
            on_active: app.press(*args, '1')
        
        MDLabel:
            size_hint_x: None
            text: ' Флажок 2'            
        MDCheckbox:
            size_hint_x: None
            size: "48dp", "48dp"
            on_active: app.press(*args, '2')              
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def press(self, checkbox, value, txt):
        if txt=='1':
            dialog = MDDialog(text="Флажок 1- " + str(value))
        else:
            dialog = MDDialog(text="Флажок 2- " + str(value))
        dialog.open()

MainApp().run()