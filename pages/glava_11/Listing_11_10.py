# Листинг 11.10
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    padding: "10dp"
    GridLayout:
        cols:3
        MDProgressBar:
            value: 50    
        MDProgressBar:
            value: 50
            orientation: "vertical"        
    MDSpinner:
        size_hint: None, None
        pos_hint: {"x": .5, "y": .5}
        size: dp(48), dp(48)        
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()