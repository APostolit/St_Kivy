# Листинг 4.6
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

KV = '''
box:
    id: root_widget
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
    ToggleButton:
        id: toggle_but
        text: 'Показать меню'
        size_hint: (None, None)
        size: (200, 75)
        pos_hint: {'center_x': .5, 'center_y': .45}
        on_press: root_widget.show_bubble(*args)
    Label:
        id: lb
        text: ''
        size_hint: (None, None)
        pos_hint: {'center_x': .5, 'center_y': .75}
    Bubble:
        id: bbl
        size_hint: (None, None)
        size: (0, 0)
        pos_hint: {'x': 1.2, 'y': 1.2}
        arrow_pos: 'top_mid'
        
        BubbleContent:
            BubbleButton:
                text: "Меню 1"
                on_press: root_widget.pressed(*args)
            BubbleButton:
                text: "Меню 2"
                on_press: root_widget.pressed(*args)
            BubbleButton:
                text: "Меню 3"
                on_press: root_widget.pressed(*args)
'''

class box(FloatLayout):
    def show_bubble(self, instance):
        if instance.text == 'Показать меню':
            self.ids['bbl'].size = (200, 50)
            self.ids['bbl'].pos_hint = {'center_x': .5,
                                        'center_y': .30}
            self.ids['toggle_but'].text = 'Скрыть меню'
        else:
            self.ids['bbl'].size = (0, 0)
            self.ids['bbl'].pos_hint = {'center_x': 1.2,
                                        'center_y': 1.2}
            self.ids['toggle_but'].text = 'Показать меню'
            self.ids['lb'].text = ''

    def pressed(self, instance):
        self.ids['lb'].text = instance.text

class BubbleApp(App):
    def build(self):
        Window.clearcolor = '#19a8ffff'
        return Builder.load_string(KV)

BubbleApp().run()