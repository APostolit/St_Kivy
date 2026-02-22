# Листинг 6.8
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class mydemoapp(App):
    text = ''
    def build(self):
        main = BoxLayout(orientation='vertical')
        self.text1 = TextInput(multiline=True, font_size=20)
        btns = BoxLayout(orientation='horizontal')

        self.b1 = Button(text='Копировать')
        self.b1.bind(on_press=self.gettext)
        self.b2 = Button(text='Вставить')
        self.b2.bind(on_press=self.insert)
        self.text2 = TextInput(
            multiline=True, font_size=20,
            foreground_color=[0, 0, 1, 1])

        btns.add_widget(self.b1)
        btns.add_widget(self.b2)
        main.add_widget(self.text1)
        main.add_widget(btns)
        main.add_widget(self.text2)
        return main

    def gettext(self, instance):
        mydemoapp.text = self.text1.selection_text

    def insert(self, instance):
        self.text2.insert_text(mydemoapp.text)

mydemoapp().run()