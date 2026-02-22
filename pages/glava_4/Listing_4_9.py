# Листинг 4.9
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.camera import Camera

class CameraApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        try:
            self.mycam = Camera(play=False)
            box.add_widget(self.mycam)
            tb = ToggleButton(text='Play', size_hint_y=None,
                              height='48dp')
            tb.bind(on_press=self.play)
            self.btn_foto = Button(text='Сделать фото',
                                   size_hint_y=None,
                                   height='48dp',
                                   on_press=self.photo)
            box.add_widget(tb)
            box.add_widget(self.btn_foto)
        except:
            box = BoxLayout(orientation='vertical')
            lab = Label(text='Видеокамера не найдена')
            box.add_widget(lab)
        return box

    def play(self, instance):
        if instance.state == 'down':
            self.mycam.play = True
            instance.text = 'Stop'
        else:
            self.mycam.play = False
            instance.text = 'Play'

    def photo(self, instance):
        self.mycam.export_to_png('photo_cam.png')

CameraApp().run()