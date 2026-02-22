# Листинг 6.7
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
Window.clearcolor = '#55555555'

class MarkApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        lb_1 = Label(
            text='[b]Жирный текст[/b] и '
                 '[color=ff3333]текст красного цвета[/color]',
            markup=True, font_size='20sp')
        box.add_widget(lb_1)
        lb_2 = Label(
            text='[u]Подчеркнутый текст[/u]',
            markup=True, font_size='20sp')
        box.add_widget(lb_2)
        lb_3 = Label(
            text='X[sub]2[/sub], Y[sup]2[/sup]',
            markup=True, font_size='20sp')
        box.add_widget(lb_3)
        return box

MarkApp().run()