# Листинг 5.14
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, ColorProperty
from kivy.uix.gridlayout import GridLayout
Window.clearcolor = '#19a8ffff'

KV = '''
Box:
    id: root_widget
    cols: 1
    Label:
        id: ttl
        text: 'Выбранный цвет'
        color: [0, 0, 0, 1]
        font_size: 32
    GridLayout:
        cols: 4        
        
        # Слайдер обработки красного цвета
        Label:            
            text: 'Красный'
        Slider:
            id: red
            min: 0
            max:255
            value: 0
            on_value: root_widget.on_red(self.value)
        Label:
            text :'Значение слайдера'
        Label:
            id: lbr
            text: '0'
        
        # Слайдер обработки зеленого цвета
        Label:            
            text: 'Зеленый'
        Slider:
            id: green
            min: 0
            max:255
            value: 0
            on_value: root_widget.on_green(self.value)
        Label:
            text :'Значение слайдера'
        Label:
            id: lbg
            text: '0'
        
        # Слайдер обработки синего цвета
        Label:            
            text: 'Синий'
        Slider:
            id: blue
            min: 0
            max:255
            value: 0
            on_value: root_widget.on_blue(self.value)
        Label:
            text :'Значение слайдера'
        Label:
            id: lbb
            text: '0'
'''

class Box(GridLayout):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)
    t = NumericProperty(1)
    colour = ColorProperty([0, 0, 0, 1])

    def on_red(self, val):
        self.r = int(val) / 255
        self.colour = [self.r, self.g, self.b, self.t]
        self.ids['ttl'].color = self.colour
        self.ids['lbr'].text = str(int(val))
    def on_green(self, val):
        self.g = int(val) / 255
        self.colour = [self.r, self.g, self.b, self.t]
        self.ids['ttl'].color = self.colour
        self.ids['lbg'].text = str(int(val))
    def on_blue(self, val):
        self.b = int(val) / 255
        self.colour = [self.r, self.g, self.b, self.t]
        self.ids['ttl'].color = self.colour
        self.ids['lbb'].text = str(int(val))

class SliderExample(App):
    def build(self):
        return Builder.load_string(KV)

SliderExample().run()