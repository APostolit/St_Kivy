# Листинг 6.10
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class Mylayout(GridLayout):
    def callback(self, *args):
        print(args[0].text)
        self.ids.l1.text = args[0].text

class TogglegroupApp(App):
    def build(self):
        return Mylayout()

TogglegroupApp().run()