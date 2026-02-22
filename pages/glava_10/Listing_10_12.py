# Листинг 10.12
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp

KV = '''
ScrollView:
    MDList:
        OneLineListItem:
            text: "Однострочный элемент"
            on_release: app.press("Элемент 1")
        TwoLineListItem:
            text: "Двухстрочный элемент"
            secondary_text: "Это вторая строк"
            on_release: app.press("Элемент 2")
        ThreeLineListItem:
            text: "Трехстрочный элемент"
            secondary_text: "Это вторая строк"
            tertiary_text: "Это третья строк"
            on_release: app.press("Элемент 3")        
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def press(self, instance):
        self.popup = Popup(title='Сделан выбор',
                           content=Label(text='Выбран: '
                                              + instance),
                           size_hint=(.8, .4))
        self.popup.open()

MainApp().run()