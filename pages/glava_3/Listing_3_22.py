# Листинг 3.22
from kivy.app import App
from kivy.lang import Builder

KV = """
<Picture@ScatterLayout>:
    source: None
    size: image.size
    size_hint: None, None
    Image:
        id: image
        source: root.source

RelativeLayout:
    canvas:
        Rectangle:
            source: 'images/Fon.jpg'
            size: self.size
            pos: self.pos
    Picture:
        source: "images/Dog.jpg"
    Picture:
        source: "images/forest.jpg"
    Picture:
        source: "images/Elena.jpg"    
"""

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()