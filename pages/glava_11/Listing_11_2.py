# Листинг 11.2
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Навигационная панель"
                        elevation: 2
                        left_action_items:
                            [['menu', lambda x: nav_drawer.set_state("open")]]
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            # Здесь будет отображаться содержимое панели
            MDScreen:
                MDFloatLayout:
                    MDLabel:
                        text: "Заголовок"
                        pos_hint: {"center_x": .8, "center_y": .9}
                    MDLabel:
                        text: "Контент 1"
                        pos_hint: {"center_x": .55, "center_y": .8}
                    MDLabel:
                        text: "Контент 2"
                        pos_hint: {"center_x": .55, "center_y": .7}
                    MDLabel:
                        text: "Контент 3"
                        pos_hint: {"center_x": .55, "center_y": .6}        

'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()