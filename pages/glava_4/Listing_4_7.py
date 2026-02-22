# Листинг 4.7
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class ButtonApp(App):
    def build(self):
        Window.clearcolor = '#19a8ffff'
        lo = StackLayout(orientation='tb-rl',
                         padding = (50, 100),
                         spacing = 10)
        b1 = Button(text='Кнопка 1', font_size=20, size_hint=(.5, .5),
                    color=[1, 0, 0, 1])
        b2 = Button(text='Кнопка 2', font_size=20, size_hint=(.5, .5),
                    background_normal='',
                    background_color='#098732ff',)
        b3 = Button(text='Python', font_size=30, size_hint=(.5, .5),
                    background_normal='pyt.png', bold=True)
        b4 = Button(text='Kivy', font_size=30, size_hint=(.5, .5),
                    background_normal='icon.png', color='#e5ff32ff',
                    bold=True)
        lo.add_widget(b1)
        lo.add_widget(b2)
        lo.add_widget(b3)
        lo.add_widget(b4)
        return lo

ButtonApp().run()