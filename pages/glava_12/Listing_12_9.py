# Листинг 12.9
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "Пример Tabs"
    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)
<Tab>
    MDLabel:
        id: label
        text: "Вкладка 0"
        halign: "center"
'''

class Tab(MDFloatLayout, MDTabsBase):
    '''Класс, реализующий содержимое для tab'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(10):
            self.root.ids.tabs.add_widget(Tab(title=f"Вкладка {i}"))

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Вызывается при переключении вкладок. '''
        instance_tab.ids.label.text = tab_text

MainApp().run()