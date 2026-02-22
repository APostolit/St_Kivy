# Листинг 4.8
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KV = '''
StackLayout:    
    orientation: 'tb-rl'
    padding: (50, 100)
    spacing: 10 
    Button:
        text: 'Кнопка 1'
        font_size: 20
        size_hint: (.5, .5)
        color: [1, 0, 0, 1]
    Button:
        text: 'Кнопка 2'
        font_size: 20
        size_hint: (.5, .5)
        background_normal: ''
        background_color: '#098732ff'
    Button:
        text: 'Python'
        font_size: 30
        size_hint: (.5, .5)
        background_down: 'pyt.png'
        bold: True
    Button:
        text: 'Kivy'
        font_size: 30
        size_hint: (.5, .5)
        background_down: 'icon.png'
        color: '#e5ff32ff'
        bold: True
'''

class ButtonApp(App):
    def build(self):
        Window.clearcolor = '#19a8ffff'
        return Builder.load_string(KV)

ButtonApp().run()