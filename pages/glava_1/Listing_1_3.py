# Листинг 1.3
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Привет от KivyMD!", halign="center")

app = MainApp(title="Приветствие от KivyMD")
app.run()