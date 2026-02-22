# Листинг 4.24
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
Window.clearcolor = '#555555'

class LblApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        l1 = Label(
            text='Метки - Label', color=[1, 0, 0, 1],
            font_size=40, bold=True)
        l2 = Label(
            text='Привет Python', color=[0, 1, 0, 1],
            font_size=40, italic=True)
        l3 = Label(
            text='Привет Kivy', color=[0, 0, 1, 1],
            font_size=40, font_name='Font/cataneo.ttf',
            underline=True)
        layout.add_widget(l1)
        layout.add_widget(l2)
        layout.add_widget(l3)
        return layout

LblApp().run()