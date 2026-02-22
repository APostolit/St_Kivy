# Листинг 6.9
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class ToggleApp(App):
    def build(self):
        self.sports = self.music = self.travel = ''

        layout = GridLayout(cols=1, padding=10)
        box = BoxLayout(orientation='horizontal')

        lbl = Label(text="Мои увлечения", font_size=16)
        layout.add_widget(lbl)

        self.l1 = Label(text='Сделайте выбор', font_size=16)
        layout.add_widget(self.l1)

        self.button1 = ToggleButton(text="Спорт", font_size=16)
        self.button2 = ToggleButton(text='Музыка', font_size=16)
        self.button3 = ToggleButton(text='Путешествия', font_size=16)

        self.button1.bind(on_press=self.btn1pressed)
        self.button2.bind(on_press=self.btn2pressed)
        self.button3.bind(on_press=self.btn3pressed)

        box.add_widget(self.button1)
        box.add_widget(self.button2)
        box.add_widget(self.button3)

        layout.add_widget(box)
        return layout

    def btn1pressed(self, instance):
        if instance.state == 'down':
            self.sports = 'Спорт'
        else:
            self.sports = ''
        self.l1.text = "{} {} {}".format(
            self.sports, self.music, self.travel)

    def btn2pressed(self, instance):
        if instance.state == 'down':
            self.music = 'Музыка'
        else:
            self.music = ''
        self.l1.text = "{} {} {}".format(
            self.sports, self.music, self.travel)

    def btn3pressed(self, instance):
        if instance.state == 'down':
            self.travel = 'Путешествия'
        else:
            self.travel = ''
        self.l1.text = "{} {} {}".format(
            self.sports, self.music, self.travel)

ToggleApp().run()