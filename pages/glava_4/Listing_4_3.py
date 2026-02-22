# Листинг 4.3.
from kivy.app import App
from kivy.uix.actionbar import (ActionBar, ActionView,
                                ActionPrevious, ActionOverflow,
                                ActionButton, ActionGroup)
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

class MainApp(App):
    def build(self):
        Window.clearcolor = '#19a8ffff'
        screen = Screen()
        # Создать метку
        self.lb = Label(text="Это текст метки",
                        font_size=20)
        screen.add_widget(self.lb)

        # Создать панель
        act_b = ActionBar(pos_hint={'bottom':1})
        screen.add_widget(act_b)

        # Создать ActionView
        act_v = ActionView(use_separator=True)
        act_b.add_widget(act_v)

        # Создать ActionPrevious
        act_pv = ActionPrevious(title='Нижняя панель',
                                with_previous=False)
        act_v.add_widget(act_pv)

        # Создать ActionOverflow
        act_over = ActionOverflow()
        act_v.add_widget(act_over)

        # Создать кнопку с иконкой
        bt_ico=ActionButton(icon='pyt.ico')
        act_v.add_widget(bt_ico)
        bt_ico.bind(on_press=self.press_but_ico)

        # Создать кнопку с текстом
        bt_txt = ActionButton(important=True,
                              text='Кнопка 1')
        bt_txt.bind(on_press=self.press_but_txt)
        act_v.add_widget(bt_txt)

        # Создать кнопку с текстом
        bt_2 = ActionButton(text='Btn2')
        act_v.add_widget(bt_2)

        # Создать группу кнопок
        group_btn = ActionGroup(text='Группа')
        bt_3 = ActionButton(text='Btn3')
        group_btn.add_widget(bt_3)
        bt_4 = ActionButton(text='Btn4')
        group_btn.add_widget(bt_4)
        act_v.add_widget(group_btn)

        return screen

    def press_but_txt(self,event):
        self.lb.text = 'Нажата кнопка c текстом'
    def press_but_ico(self,event):
        self.lb.text = 'Нажата кнопка с иконкой'

MainApp().run()