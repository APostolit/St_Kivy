# Листинг 6.5
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.switch import Switch
from kivy.core.window import Window

Window.clearcolor = '#19a8ffff'

class SwitchApp(App):
    def build(self):
        box = BoxLayout(orientation='horizontal')
        self.l1 = Label(
           text = 'Выключен',
           font_size = 16)
        box.add_widget(self.l1)
        switch = Switch()
        switch.bind(active = self.switched)
        box.add_widget(switch)
        return box

    def switched(self, instance, value):
        if value == True:
            self.sound = SoundLoader.load('audio/gaiti.mp3')
            self.l1.text = 'Включен'
            self.sound.play()
        else:
            self.sound.stop()
            self.l1.text = 'Выключен'

SwitchApp().run()