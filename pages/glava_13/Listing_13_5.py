# Листинг 13.5
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
Window.size = (400, 600)

class My_ShopApp(MDApp):
    k_kol = 0
    k_sum = 0
    k_list = ''
    zakaz = ''

    def build(self):
        kv_file = 'Pizza_Delivery.kv'
        return Builder.load_file(kv_file)

    def menu_up(self):
        MDDialog(text='Нажата кнопка меню верхней панели').open()

    def menu_down(self):
        MDDialog(text='Нажата кнопка меню нижней панели').open()

    def email(self):
        MDDialog(text='Нажата кнопка почта').open()

    def phone(self):
        MDDialog(text='Нажата кнопка телефон').open()

    def on_my_icon(self):
        MDDialog(text=self.zakaz).open()

    def on_touch_down(self, card):
        self.k_kol = self.k_kol + 1
        self.k_list = self.k_list + card + ', '
        self.zakaz = 'В заказе -' + str(self.k_kol) + ':' + self.k_list
        MDDialog(text=self.zakaz).open()

My_ShopApp().run()