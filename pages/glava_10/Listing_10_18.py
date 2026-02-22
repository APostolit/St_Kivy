# Листинг 10.18
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu

KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "Меню в MDToolbar"
        left_action_items: [["menu", lambda x: app.callback_l(x)]]
        right_action_items: [["dots-vertical", lambda x: app.callback_r(x)]]
    MDLabel:
        text: "Основное окно приложения"
        halign: "center"
'''

class MainApp(MDApp):
    def build(self):
        # опции меню левой кнопки
        menu_items = [{"text": "Меню левое 1",
                       "viewclass": "OneLineListItem",
                       "on_release": lambda x="Меню левое 1": self.dialog(x), },
                      {"text": "Меню левое 2",
                       "viewclass": "OneLineListItem",
                       "on_release": lambda x="Меню левое 2": self.dialog(x), },
                      {"text": "Меню левое 3",
                       "viewclass": "OneLineListItem",
                       "on_release": lambda x="Меню левое 3": self.dialog(x), },
                      ]
        self.menu = MDDropdownMenu(items=menu_items, width_mult=2.5, )

        # опции меню правой кнопки
        menu_items_r = [{"text": "Меню правое 1",
                       "viewclass": "OneLineListItem",
                       "on_release": lambda x="Меню правое 1": self.dialog(x), },
                      {"text": "Меню правое 2",
                       "viewclass": "OneLineListItem",
                       "on_release": lambda x="Меню правое 2": self.dialog(x), },
                      {"text": "Меню правое 3",
                       "viewclass": "OneLineListItem",
                       "on_release": lambda x="Меню правое 3": self.dialog(x), },
                      ]
        self.menu_r = MDDropdownMenu(items=menu_items_r, width_mult=2.5, )
        return Builder.load_string(KV)

    # Открыть левое меню ##################
    def callback_l(self, button):
        self.menu.caller = button
        self.menu.open()
    # Открыть правое меню #################
    def callback_r(self, button):
        self.menu_r.caller = button
        self.menu_r.open()
    # Обработка опций меню #################
    def dialog(self, text):
        dialog = MDDialog(text='Выбрано: '+  text)
        dialog.open()

MainApp().run()