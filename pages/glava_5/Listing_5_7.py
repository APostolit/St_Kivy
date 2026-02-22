# Листинг 5.7
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = '''
Box:
    id: root_widget
    orientation: 'vertical'
    orientation: 'vertical'
    ProgressBar:
        id: pb
        max: 100
        value: 0
    Button:
        id: btn
        text: 'Старт'
        size_hint: (0.2, 0.2)
        pos_hint: {"center_x": .5}
        on_press: root_widget.start(*args)
'''
Window.clearcolor = '#33333333'

class Box(BoxLayout):
    def start(self, instance):
        self.ids['pb'].value = 0
        self.increment = 10
        # Обновление каждые 0.5 секунды
        Clock.schedule_interval(self.update_progress, 0.5)

    def update_progress(self, dt):
        if self.ids['pb'].value < 100:
            # Увеличение значения индикатора
            self.ids['pb'].value  += self.increment
        else:
            # Остановить обновление индикатора
            return False

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()