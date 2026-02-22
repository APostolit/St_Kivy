# Листинг 6.1
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class splitterApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        # Кнопка 1
        b1 = Button(
            text='Кнопка 1',
            font_size=16, color=(1, 0, 0, 1))
        layout.add_widget(b1)
        # Разделитель
        spl = Splitter(sizable_from='left')
        img = Image(source='icon.png')
        spl.add_widget(img)
        layout.add_widget(spl)
        # Кнопка 2
        b2 = Button(
            text='Кнопка 2', font_size=16,
            background_color=(.8, .4, .3, 1)
        )
        layout.add_widget(b2)
        return layout

splitterApp().run()