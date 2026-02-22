# Листинг 2.18
from kivy.app import App  # импорт класса - приложения
from kivy.lang import Builder  # импорт метода Builder

# Создание текстовой строки с кодом KV
my_str = '''
Label:
    text:('Текст метки')
    font_size: '16pt'
'''

# Загрузка кода из текстовой строки
kv_str = Builder.load_string(my_str)

# Определение базового класса
class Basic_Class(App):
    def build(self):
        return kv_str

# Приложение на основе базового класса
My_App = Basic_Class()
# Запуск приложения
My_App.run()