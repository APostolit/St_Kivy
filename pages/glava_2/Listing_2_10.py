# Листинг 2.10
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = '''
box:
    orientation: 'vertical' 
    Button:
        size_hint: (.5, .1)
        pos_hint: {'center_x': .5, 'center_y': .9}      
        text: ' Кнопка '
        on_press: root.result('Нажата кнопка')
    Label:
        id: itog
        pos_hint: {'center_x': .5, 'center_y': .5}
'''

class box(BoxLayout):
    def result(self, entry_text):
        self.ids["itog"].text = entry_text

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()