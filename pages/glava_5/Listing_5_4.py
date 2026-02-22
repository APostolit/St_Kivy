# Листинг 5.4
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text:'Открыть'
        font_size: 16        
        pos_hint: {'center_x': .5, 'center_y': .3}
        size_hint: (.3, None)
        size: (100, 50)
        on_press: app.show_modal(self.text)
'''
Window.clearcolor = '#19a8ffff'

class ModalViewApp(App):
    def build(self):
        return Builder.load_string(KV)

    def show_modal(self, instance):
        # Модальное окно
        view = ModalView(auto_dismiss=False, size_hint=(None, None),
                         size=(300, 150))
        grid = GridLayout(cols=1, padding=20)
        # Метка в модальном окне
        grid.add_widget(Label(text='Это модальное окно', font_size=16,
                              color=[1, 0, 0, 1]))
        # Кнопка в модальном окне
        btn = Button(
            text='Закрыть', font_size=16, size_hint=(None, None),
            size=(100, 50), on_press=view.dismiss)
        grid.add_widget(btn)
        view.add_widget(grid)
        view.open()

ModalViewApp().run()