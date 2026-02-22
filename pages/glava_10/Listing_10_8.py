# Листинг 10.8
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
ScrollView:
    MDGridLayout:
        cols: 2
        row_default_height: 
            (self.width - self.cols*self.spacing[0])+1 / self.cols
        row_force_default: True
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)     

        MDSmartTile:                    
            source: "images/Ballon.jpg"
            on_release: app.press('Ballon')
            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
            MDLabel:
                text: "Ballon"
                theme_text_color: "Custom"
                text_color: "white"

        MDSmartTile:
            source: "images/Elena.jpg"
            on_release: app.press('Elena')
            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
            MDLabel:
                text: "Elena"
                theme_text_color: "Custom"
                text_color: "white"

        MDSmartTile:
            source: "images/Flora.jpg"
            on_release: app.press('Flora')
            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
            MDLabel:
                text: "Flora"
                theme_text_color: "Custom"
                text_color: "white"

        MDSmartTile:
            source: "images/Fortuna.jpg"
            on_release: app.press('Fortuna')
            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
            MDLabel:
                text: "Fortuna"
                theme_text_color: "Custom"
                text_color: "white"

        MDSmartTile:
            source: "images/Ganna.jpg"
            on_release: app.press('Ganna')
            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
            MDLabel:
                text: "Ganna"
                theme_text_color: "Custom"
                text_color: "white"

        MDSmartTile:
            source: "images/Gorox.jpg"
            on_release: app.press('Gorox')
            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
            MDLabel:
                text: "Gorox"
                theme_text_color: "Custom"
                text_color: "white"
'''
class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def press(self, instance):
        self.popup = Popup(title='Сделан выбор',
                           content=Label(text='Выбрано платье: '
                                              + instance),
                           size_hint=(.8, .4))
        self.popup.open()

MyApp().run()