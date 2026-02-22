# Листинг 10.14
from kivymd.app import MDApp
from kivy.lang.builder import Builder

kv = '''
MDScreen:
    MDTopAppBar:
        id: toolbar
        title: "Пример MDSwiper"
        elevation: 2
        pos_hint: {"top": 1}
    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(20)
        y: root.height - self.height - toolbar.height - dp(10)

        MDSwiperItem:
            FitImage:
                source: "images/Ballon.jpg"
                radius: [10,]
        MDSwiperItem:
            FitImage:
                source: "images/Elena.jpg"
                radius: [10,]
        MDSwiperItem:
            FitImage:
                source: "images/Flora.jpg"
                radius: [10,]
        MDSwiperItem:
            FitImage:
                source: "images/Fortuna.jpg"
                radius: [10,]

        MDSwiperItem:
            FitImage:
                source: "images/Gorox.jpg"
                radius: [10,]
'''

class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)

Main().run()