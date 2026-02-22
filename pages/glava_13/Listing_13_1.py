# Листинг 13.1
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    # создание интерфейса
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        # создание пользовательского класса
        # основного контейнера на базе класса BoxLayout
        main_layout = BoxLayout(orientation="vertical")

        # создание пользовательского класса
        # для ввода текста на основе TextInput
        self.solution = TextInput(multiline=False,
                                  readonly=True,
                                  halign="right",
                                  font_size=55)

        # размещение в главном контейнере
        # текстового поля для отображения итогов
        main_layout.add_widget(self.solution)
        # формирование массива кнопок с цифрами и действиями
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        # цикл по столбцам
        for row in buttons:
            # создание объекта-контейнера для кнопок
            h_layout = BoxLayout()
            # цикл по строкам
            for label in row:
                # создание объекта - кнопка
                button = Button(text=label,
                                pos_hint={"center_x": 0.5, "center_y": 0.5},)
                # привязка кнопки к функции обработки нажатия
                button.bind(on_press=self.on_button_press)
                # добавление кнопки в контейнер
                h_layout.add_widget(button)

            # вложение контейнера с кнопками в главный контейнер
            main_layout.add_widget(h_layout)

        # создание кнопки расчета итогов (=)
        equals_button = Button(text="=",
                               pos_hint={"center_x": 0.5, "center_y": 0.5})
        # привязка кнопки (=) к функции обработки нажатия
        equals_button.bind(on_press=self.on_solution)
        # добавление кнопки равно к главному контейнеру
        main_layout.add_widget(equals_button)
        return main_layout

    # обработка нажатий клавиш на клавиатуре
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        # очистить итог вычислений
        if button_text == "C":
            self.solution.text = ""
        else:
            # если добавлены два оператора сразу друг за другом
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # Если первый символ оператор а не цифра
            elif current == "" and button_text in self.operators:
                return
            # если все правильно
            else:
                new_text = current + button_text
                self.solution.text = new_text

        # вывод результатов набора операций в текстовое поле
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    # нажата клавиша (=)
    def on_solution(self, instance):
        text = self.solution.text
        # вывод результатов расчета в текстовое поле
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == "__main__":
    app = MainApp()
    app.run()