# Листинг 11.5
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "Навигационная рейка"
    MDBoxLayout:
        # навигационная рейка
        MDNavigationRail:
            id: rail
            md_bg_color: get_color_from_hex("#344954")
            color_normal: get_color_from_hex("#718089")
            color_active: get_color_from_hex("#f3ab44")            
            #элементы навигационной рейки
            MDNavigationRailItem:
                icon: "language-cpp"
                text: "C++"
                on_press: app.press("C++")
            MDNavigationRailItem:
                icon: "language-python"
                text: "Python"
                on_press: app.press("Python")
            MDNavigationRailItem:
                icon: "language-swift"
                text: "Swift"
                on_press: app.press("Swift")
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def press(self, text_item):
        dialog = MDDialog(text="Выбрано " + text_item)
        dialog.open()

MainApp().run()