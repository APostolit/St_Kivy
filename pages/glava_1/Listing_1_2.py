# Листинг 1.2
import kivy.app
# Импорт визуального элемента label (метка)
import kivy.uix.label

# Формирование базового класса приложения
class MainApp(kivy.app.App):
    # Формирование функции в базовом классе
    def build(self):
        return kivy.uix.label.Label(text="Привет от Kivy!")

# Задание имени приложеня
app = MainApp(title="Периветисвие от Kivy")
app.run()  # запуск приложения