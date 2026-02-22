# Листинг 12.21
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip

KV = '''
MDScreen:
    TooltipMDIconButton:
        icon: "language-python"
        tooltip_text: "Язык программирования Python"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()