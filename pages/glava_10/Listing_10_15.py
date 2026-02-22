# Листинг 10.15
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog

kv = '''
<MagicButton@MagicBehavior+MDIconButton>
MDScreen:
    MDTopAppBar:
        id: toolbar
        title: "Пример MDSwiper"
        elevation: 10
        pos_hint: {"top": 1}

    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(20)
        y: root.height - self.height - toolbar.height - dp(10)

        MDSwiperItem:
            RelativeLayout:
                FitImage:
                    source: "images/Elena.jpg"
                    radius: [10,]
                MDBoxLayout:
                    adaptive_height: True
                    spacing: "12dp" 
                    MagicButton:
                        id: icon
                        icon: "weather-sunny"
                        user_font_size: "56sp"
                        on_press: app.dialog('Елена')
                    MDLabel:
                        text: "Платье Елена"
                        font_style: "H5"
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
        MDSwiperItem:
            RelativeLayout:
                FitImage:
                    source: "images/Fortuna.jpg"
                    radius: [10,]
                MDBoxLayout:
                    adaptive_height: True
                    spacing: "12dp" 
                    MagicButton:
                        id: icon
                        icon: "weather-sunny"
                        user_font_size: "56sp"
                        on_press: app.dialog('Фортуна')
                    MDLabel:
                        text: "Платье Фортуна"
                        font_style: "H5"
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
        MDSwiperItem:
            RelativeLayout:
                FitImage:
                    source: "images/Gorox.jpg"
                    radius: [10,]
                MDBoxLayout:
                    adaptive_height: True
                    spacing: "12dp" 
                    MagicButton:
                        id: icon
                        icon: "weather-sunny"
                        user_font_size: "56sp"
                        on_press: app.dialog('Горох')
                    MDLabel:
                        text: "Платье Горох"
                        font_style: "H5"
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
'''

class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def dialog(self, text):
        dialog = MDDialog(text='Выбрано: '+  text)
        dialog.open()

Main().run()