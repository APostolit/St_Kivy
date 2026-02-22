# Листинг 4.25
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
Window.clearcolor = '#555555'

KV = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'Метки - Label'
        color: [1, 0, 0, 1]
        font_size: 40
        bold: True
    Label:
        text: 'Привет Python'
        color: [0, 1, 0, 1]
        font_size: 40
        italic: True
    Label:
        text: 'Привет Kivy'
        color: [0, 0, 1, 1]
        font_size: 40
        font_name: 'Font/cataneo.ttf'
        underline:True        
'''

class LblApp(App):
    def build(self):
        return Builder.load_string(KV)

LblApp().run()