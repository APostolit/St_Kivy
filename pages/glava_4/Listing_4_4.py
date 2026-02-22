# Листинг 4.4
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

KV = '''
ActionBar:
    # pos_hint: {'bottom':1}
    pos_hint: {'top':1}
    ActionView:
        use_separator: True        
        ActionPrevious:
            title: 'Верхняя панель'
            with_previous: False        
        ActionOverflow:        
        ActionButton:
            icon: 'pyt.ico'        
        ActionButton:
            important: True
            text: 'Кнопка 1'
            on_press: app.press_button(*args)        
        ActionButton:
            text: 'Btn2'        
        ActionGroup:
            text: 'Группа'
            ActionButton:
                text: 'Btn3'
            ActionButton:
                text: 'Btn4'           
'''

class MainApp(App):
    def build(self):
        Window.clearcolor = '#19a8ffff'
        return Builder.load_string(KV)

    def press_button(self, instance):
        self.popup = Popup(title='Модальное окно',
                           content=Label(text=str(instance.text)),
                           size_hint=(.8, .4))
        self.popup.open()

MainApp().run()