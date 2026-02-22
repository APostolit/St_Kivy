# Листинг 4.10
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

KV = '''
Box:
    id: root_widget
    orientation: 'vertical'
    Camera:
        id: camera        
        play: False
    ToggleButton:
        text: 'Play'        
        size_hint_y: None
        height: '48dp'
        on_press: root_widget.play(*args)
    Button:
        text: 'Сделать фото'
        size_hint_y: None
        height: '48dp'
        on_press: root_widget.photo(*args)
'''

class Box(BoxLayout):
    def play(self, instance):
        if instance.state == 'down':
            self.ids['camera'].play = True
            instance.text = 'Stop'
        else:
            self.ids['camera'].play = False
            instance.text = 'Play'

    def photo(self, instance):
        self.ids['camera'].export_to_png('photo_cam.png')

class CameraApp(App):
    def build(self):
        try:
            return Builder.load_string(KV)
        except:
            box = BoxLayout(orientation='vertical')
            lab = Label(text='Видеокамера не найдена')
            box.add_widget(lab)
            return box
CameraApp().run()