# Листинг 4.21
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Класс для разметки страниц приложения
class Filechooser(BoxLayout):
    def select(self, *args):
        try:
            self.label.text = args[1][0]
        except:
            pass

# Класс для приложения
class FileApp(App):
    def build(self):
        return Filechooser()

FileApp().run()