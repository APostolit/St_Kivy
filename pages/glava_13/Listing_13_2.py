# Листинг 13.2
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

# Установка размера окна
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

# Создание класса - контейнера
class CalcGridLayout(GridLayout):
    # Функция, вызываемая при нажатии кнопки равно
    def calculate(self, calculation):
        if calculation:
            try:
                # Формула для расчета результатов
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Ошибка"

# Создание класса - приложение
class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

# Создание объекта "Приложение" и запуск его
calcApp = CalculatorApp()
calcApp.run()