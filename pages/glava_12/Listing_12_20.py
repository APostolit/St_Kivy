# Листинг 12.20
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
<TooltipMDIconButton@MDIconButton+MDTooltip>
Screen:
    TooltipMDIconButton:
        icon: "language-python"
        tooltip_text: "Язык программирования Python"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()