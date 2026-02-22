# Листинг 4.16
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

KV = '''
Box:
    id: root_w
    orientation: 'vertical'
    # Выбор пола
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: 'Пол: '
        Label:
            text: 'Мужчина'
        CheckBox:
            id: m
            group: 'sex'
            on_press: root_w.on_sex_m(*args)
        Label:
            text: 'Женщина'
        CheckBox:
            id: f
            on_press: root_w.on_sex_f(*args)
            group: 'sex'
    Label:
        id: lb_sex
        text:"Выбран пол: "
        font_size: 16
    
    # Выбор интереса
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Интересы:'
        Label:
            id: lb_sport
            text: 'Спорт'
        CheckBox:
            id: sport
            on_press: root_w.on_interest(*args)
        Label:
            text: 'Музыка'
        CheckBox:
            id: muz
            on_press: root_w.on_interest(*args)
        Label:
            text: 'Туризм'
        CheckBox:
            id: tur
            on_press: root_w.on_interest(*args)
        Label:
            id: label
            text: "Выбран интерес: "
            font_size: 16     
'''
class Box(BoxLayout):
    def on_sex_m(self, value):
        self.ids['lb_sex'].text = "Выбран пол: Мужчины"

    def on_sex_f(self, value):
        self.ids['lb_sex'].text = "Выбран пол: Женщины"

    def on_interest(self, value):
        CheckBoxApp.intrst = []
        if self.ids['sport'].active:
            CheckBoxApp.intrst.append("Спорт")
        if self.ids['muz'].active:
            CheckBoxApp.intrst.append("Музыка")
        if self.ids['tur'].active:
            CheckBoxApp.intrst.append("Туризм")
        self.ids['label'].text = ("Выбран интерес: " +
                                  " ".join(CheckBoxApp.intrst))

class CheckBoxApp(App):
    Window.clearcolor = '#555555'
    def build(self):
        return Builder.load_string(KV)

CheckBoxApp().run()