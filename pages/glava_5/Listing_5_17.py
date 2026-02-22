# Листинг 5.17
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
Window.clearcolor = '#19a8ffff'

KV = '''
TabbedPanel:
    size_hint: .8, .8
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False       
      
    TabbedPanelItem:  
        text:"Регистрация"        
        GridLayout:
            cols:2                 
            Label:
                text:"Логин"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.75}
            TextInput:
                size_hint:(.4, .1)
                pos_hint:{'x':.3, 'y':.65}
            Label:
                text:"e-mail"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.55}
            TextInput:
                size_hint:(.4, .1)
                pos_hint:{'x':.3, 'y':.45}
            Label:
                text:"Пароль"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.35}
            TextInput:
                password:True
                size_hint:(.4, .1)
                pos:(400, 150)
                pos_hint:{'x':.3, 'y':.25}
            Button:
                text:'Принять'
                size_hint : (.2, .1)
                pos_hint : {'center_x':.5, 'center_y':.09}

    TabbedPanelItem:
        text:'Вход'
        GridLayout:
            cols:2      
            Label:
                text:"Логин"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.55}
            TextInput:
                size_hint:(.4, .1)
                pos_hint:{'x':.3, 'y':.45}
            Label:
                text:"Пароль"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.35}
            TextInput:
                password:True
                size_hint:(.4, .1)
                pos:(400, 150)
                pos_hint:{'x':.3, 'y':.25}
            Button:
                text:'Принять'
                size_hint : (.2, .1)
                pos_hint : {'center_x':.5, 'center_y':.09}
'''

class TabDemoApp(App):
    def build(self):
        return Builder.load_string(KV)

TabDemoApp().run()