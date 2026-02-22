# Листинг 2.11
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = '''
box:
    # Корневой виджет
    id: root_widget
    orientation: 'vertical'

    # Поле для ввода исходных данных
    TextInput:
        id: entry
        font_size: 32
        multiline: False

    # Кнопка для выполнения расчета
    Button:
        text: ' = '
        font_size: 64        
        on_press: root_widget.result(entry.text)

    # Поле для показа результатов расчета
    Label:
        id: itog
        text: 'Итого' 
        font_size: 32   
'''

# Класс, задающий корневой виджет
class box(BoxLayout):
    # Функция подсчета результата
    def result(self, entry_text):
        if entry_text:
            try:
                # Формула для расчета результатов
                result = str(eval(entry_text))
                self.ids["itog"].text = result
            except Exception:
                # если введено не число
                self.ids["itog"].text = "Ошибка"

# Базовый класс приложения
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()