# Листинг 12.10
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase

KV = '''
BoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        left_action_items: [["menu", lambda x: x]]
        title: "Модели платьев"
    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)
        Tab:
            icon: 'account-check'
            title: 'Флора'
            Image:
                source: 'images/Flora.jpg'               
        Tab:
            icon: 'account-check'
            title: 'Елена'
            Image:
                source: 'images/Elena.jpg'               
        Tab:
            icon: 'account-check'
            title: 'Фортуна'
            Image:
                source: 'images/Fortuna.jpg'              
'''

class Tab(FloatLayout, MDTabsBase):
    pass
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def on_tab_switch(self, instance_tabs, instance_tab,
                      instance_tab_label, title):
       pass

MainApp().run()