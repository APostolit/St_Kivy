# Листинг 4.23
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

KV = '''
Carousel:
    direction:'top'
    Image:
        source:'images/Flora.jpg'      
        fit_mode:"scale-down"
        Label:
            text: 'scale-down'        
    Image:
        source:"images/Flora.jpg"
        fit_mode:"contain"
        Label:
            text: 'contain'
    Image:
        source:"images/Flora.jpg"
        fit_mode:"fill"
        Label:
            text: 'fill'
    Image:
        source:"images/Flora.jpg"
        fit_mode:"cover"
        Label:
            text: 'cover'
'''
Window.clearcolor = '#19a8ffff'

class W_image(App):
    def build(self):
        return Builder.load_string(KV)

W_image().run()
