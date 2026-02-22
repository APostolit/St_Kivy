# Листинг 4.11
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Ellipse

class CanvasApp(App):
    def build(self):
        widget = Widget()
        with widget.canvas:
            # Нарисовать прямоугольник
            Color(0, 0, 1, 1)
            Rectangle(pos=(50, 300),
                      size_hint=(None, None),
                      size=(300, 200))
            # Нарисовать круг
            Color(1, 0, 0, 1)
            d = 100
            Ellipse(pos=(500, 150), size=(d, d))
            # Вывести изображение
            Color(.5, .5, .5)
            Rectangle(source='icon.png', pos=(50, 150))
            Color(1, 1, 1)
            # Вывести метку
            lbl = Label(
                text='Привет Kivy', font_size=24,
                pos=(Window.width / 2, 300), size=(200, 200),
                color=(0, 0, 1, 1))
            with lbl.canvas.before:
                Color(1, 1, 0)
                Rectangle(pos=lbl.pos, size=lbl.size)
            widget.add_widget(lbl)
        return widget

CanvasApp().run()