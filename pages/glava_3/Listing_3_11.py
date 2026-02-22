## Листинг 3.11
from kivy.app import App
from kivy.lang import Builder

# создание текстовой строки
KV = """
GridLayout:
    cols: 2 
    rows: 2

    Button:
        text: 'Кнопка 1 KV'
    Button:
        text: 'Кнопка 2 KV'
    Button:
        text: 'Кнопка 3 KV'
    Button:
        text: 'Кнопка 4 KV'
"""

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()