# Листинг 12.5
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarActionButton

KV = '''
MDScreen:
    MDRaisedButton:
        text: "Открыть Snackbar"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.press(self.text)       
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def press(self, instance):
        MDSnackbar(MDLabel(text="Нижняя панель",),
                   MDSnackbarActionButton(text="Кнопка панели",
                                          theme_text_color="Custom",
                                          text_color="#8E353C",),
                   pos_hint={"center_x": 0.5},
                   size_hint_x=0.5,
                   md_bg_color="#64b5f6ff",).open()

MainApp().run()