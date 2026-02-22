# Листинг 4.15
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = '#555555'

class CheckBoxApp(App):
    gender = ''
    intrst = []

    def build(self):
        # Главное окно
        main = BoxLayout(orientation='vertical')
        # Гендерная группа связанных радио кнопок
        gender_grp = BoxLayout(orientation='horizontal')

        # Выбор мужчин -----------------------
        gender_grp.add_widget(Label(text='Пол:'))
        # Метка
        self.lb_m = Label(text='Мужчина')
        gender_grp.add_widget(self.lb_m)
        # Кнопка выбора
        self.m = CheckBox(group='sex')
        self.m.bind(active=self.on_sex_m)
        gender_grp.add_widget(self.m)

        # Выбор женщин -------------------------
        self.lb_f = Label(text='Женщина')
        gender_grp.add_widget(self.lb_f)
        self.f = CheckBox(group='sex')
        self.f.bind(active=self.on_sex_f)
        gender_grp.add_widget(self.f)

        # Добавить гендерные кнопки в главное окно
        main.add_widget(gender_grp)

        # Добавить метку гендерного выбора в главное окно
        self.lbl = Label(text="Выбран пол: ", font_size=16)

        interests = BoxLayout(orientation='vertical')
        main.add_widget(self.lbl)
        interests.add_widget(Label(text='Интересы:'))
        interests.add_widget(Label(text='Спорт'))
        self.cb1 = CheckBox()
        self.cb1.bind(active=self.on_interest)
        interests.add_widget(self.cb1)

        self.cb2 = CheckBox()
        self.cb2.bind(active=self.on_interest)
        interests.add_widget(Label(text='Музыка'))
        interests.add_widget(self.cb2)

        self.cb3 = CheckBox()
        self.cb3.bind(active=self.on_interest)
        interests.add_widget(Label(text='Туризм'))
        interests.add_widget(self.cb3)

        self.lbl1 = Label(text="Выбран интерес: ", font_size=16)
        main.add_widget(interests)
        main.add_widget(self.lbl1)
        return main

    def on_sex_m(self, instance, value):
        self.lbl.text = "Выбран пол: " + self.lb_m.text

    def on_sex_f(self, instance, value):
        self.lbl.text = "Выбран пол: " + self.lb_f.text

    # Выбран интерес
    def on_interest(self, instance, value):
        CheckBoxApp.intrst = []
        if self.cb1.active:
            CheckBoxApp.intrst.append("Спорт")
        if self.cb2.active:
            CheckBoxApp.intrst.append("Музыка")
        if self.cb3.active:
            CheckBoxApp.intrst.append("Туризм")
        self.lbl1.text = ("Выбран интерес: " +
                          " ".join(CheckBoxApp.intrst))

CheckBoxApp().run()