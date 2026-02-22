# Листинг 4.12
from kivy.app import App
from kivy.lang import Builder

KV = '''
Widget:
    canvas:        
        Color:
            rgb: (1,1,0)
        Rectangle:
            pos: (50, 300)            
            size: (300, 200)
        Color:
            rgb: (1,0,0)            
        Ellipse:
            pos: (500, 150)
            size: (100, 100)
        Color:
            rgb: (.5,.5,.5)
        Rectangle:
            source: 'icon.png'
            pos: (50, 150)            
'''

class CameraApp(App):
    def build(self):
        return Builder.load_string(KV)
CameraApp().run()