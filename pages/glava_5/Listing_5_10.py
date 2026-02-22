# Листинг 5.10
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

KV = """
Scatter:   
    Label:       
        text: "Метка"
        font_size: 60
"""
Window.clearcolor = '#19a8ffff'

class Myscatter(App):
    def build(self):
        return Builder.load_string(KV)

Myscatter().run()