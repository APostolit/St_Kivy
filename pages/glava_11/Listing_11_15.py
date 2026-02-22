# Листинг 11.15
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

KV = '''
MDFloatLayout:
    MDSwitch:
        width: dp(64)
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_active: app.active(*args)   
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def active(self, switch, value):
        if value == True:
            status = "Включен"
        else:
            status = "Выключен"
        dialog = MDDialog(text="Переключатель- " + status)
        dialog.open()

Test().run()