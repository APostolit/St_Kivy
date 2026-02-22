# Листинг 5.16
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class SpinnerExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        lo1 = BoxLayout(orientation='horizontal')
        self.spin1 = Spinner(
            text='Русский',
            values=("Русский", "Английский", "Немецкий",
                    "Французский", "Итальянский", "Испанский"),
            background_color=(0, 1, 0, 1),
            size_hint=(.5, .4), pos_hint={'top': 1}
        )
        self.spin1.bind(text=self.on_spinner_select)

        lo1.add_widget(self.spin1)
        self.spinnerSelection = Label(
            text="Выбран язык: %s" % self.spin1.text,
            pos_hint={'top': 1, 'x': .4}
        )
        lo1.add_widget(self.spinnerSelection)
        layout.add_widget(lo1)
        lo2 = BoxLayout(orientation='horizontal')
        layout.add_widget(lo2)
        return layout

    def on_spinner_select(self, spinner, text):
        self.spinnerSelection.text = "Выбран язык: %s" % self.spin1.text

SpinnerExample().run()