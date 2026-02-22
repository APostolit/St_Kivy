# Листинг 2.16
from kivy.app import App  # импорт класса - приложения
from kivy.lang import Builder  # импорт метода Builder

# Загрузка кода из KV файла
kv_file = Builder.load_file('main_screen.kv')

# Определение базового класса
class Basic_Class(App):
    def build(self):
        return kv_file

# Приложение на основе базового класса
My_App = Basic_Class()
# Запуск приложения
My_App.run()