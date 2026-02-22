# Листинг 6.6
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.size = (720, 400)

class CustomFontApp(App):
    def build(self):
        main = GridLayout(cols=1)
        LabelBase.register(name='font1',
                           fn_regular='Font/cataneo.ttf')
        LabelBase.register(name='font2',
                           fn_regular='Font/EmilyAustin.ttf')
        txt = 'Для вывода этого текста использовался разный фонт'
        txt1 = 'Different fonts were used to display this text'
        t1 = TextInput(text=txt, halign='center', font_size=48)
        t2 = TextInput(
            text=txt1, halign='center',
            font_name='font2', font_size=48
        )
        t3 = TextInput(
            text=txt, halign='center',
            font_name='font1', font_size=48
        )
        main.add_widget(t1)
        main.add_widget(t2)
        main.add_widget(t3)
        return main

CustomFontApp().run()