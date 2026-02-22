# Листинг 2.15
from kivy.app import App
from kivy.lang import Builder

# Файл разметки на Kivy
kv_file = Builder.load_file('basic_class.kv')

# Определение базового класса
class Basic_Class(App):
    def build(self):
        return kv_file

# Приложение на основе базового класса
My_App = Basic_Class()
# Запуск приложения
My_App.run()