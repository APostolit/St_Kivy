# Листинг 5.6
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
Window.clearcolor = '#33333333'

class MyApp(App):
    def build(self):
        # Макет страницы
        layout = BoxLayout(orientation='vertical')
        # Создание progress bar
        self.progress_bar = ProgressBar(max=100, value=0)
        # Кнопка старта
        button = Button(text='Старт', size_hint=(0.2, 0.2),
                        pos_hint = {"center_x": .5})
        button.bind(on_press=self.start_task)

        layout.add_widget(self.progress_bar)
        layout.add_widget(button)
        return layout

    def start_task(self, instance):
        self.progress_bar.value = 0
        self.increment = 10
        # Обновление каждые 0.5 секунды
        Clock.schedule_interval(self.update_progress, 0.5)

    def update_progress(self, dt):
        if self.progress_bar.value < 100:
            # Увеличение значения индикатора
            self.progress_bar.value += self.increment
        else:
            # Остановить обновление индикатора
            return False

MyApp().run()