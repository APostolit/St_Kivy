# Листинг 5.3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class ModalViewApp(App):
   def show_modal(self, obj):
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

   def build(self):
      btn = Button(
         text='Открыть', font_size=16, on_press=self.show_modal,
         pos_hint={'center_x': .5, 'center_y': .2},
         size_hint=(.3, None), size=(100, 50))
      return btn
ModalViewApp().run()