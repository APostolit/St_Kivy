# Листинг 10.1
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen
    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: 'Элемент 1'
        on_release: self.set_item("Элемент 1 после раскрытия")
    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': .5, 'center_y': .4}
        text: 'Элемент 2'
        on_release: self.set_item("Элемент 2 после раскрытия")
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()