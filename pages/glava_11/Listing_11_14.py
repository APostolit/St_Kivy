# Листинг 11.14
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

KV = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)
FloatLayout:
    Check:
        active: True
        pos_hint: {'center_x': .3, 'center_y': .5}
        on_active: app.active('1')    
    Check:
        pos_hint: {'center_x': .5, 'center_y': .5} 
        on_active: app.active('2')       
    Check:
        pos_hint: {'center_x': .7, 'center_y': .5}
        on_active: app.active('3')
    MDRaisedButton:
        id: btn
        text: "Кнопка"
        pos_hint: {'center_x': .5, 'center_y': .3}
        on_press: app.bt_press(self)         
'''

class MainApp(MDApp):
    def build(self):
        self.activ = 1
        return Builder.load_string(KV)
    def active(self, txt):
        if txt=='1':
            self.activ = 1
        elif txt=='2':
            self.activ = 2
        elif txt=='3':
            self.activ = 3

    def bt_press(self, checkbox,):
        dialog = MDDialog(text="Активен флажок- " + str(self.activ))
        dialog.open()

MainApp().run()