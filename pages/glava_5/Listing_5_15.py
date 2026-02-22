# Листинг 5.15
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class audioapp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10)
        self.l1 = Label(text='Нажмите Старт',
                        font_size=20)
        layout.add_widget(self.l1)
        box = BoxLayout(orientation='horizontal')
        self.button1 = Button(text="Старт", font_size=16)
        self.button2 = Button(text='Пауза', font_size=16,
                              disabled=True)
        box.add_widget(self.button1)
        box.add_widget(self.button2)
        layout.add_widget(box)
        self.button1.bind(on_press=self.start_stop)
        self.button2.bind(on_press=self.pause_resume)
        return layout

    def start_stop(self, event):
        if self.button1.text == 'Старт':
            self.l1.text = 'Проигрывание'
            self.button1.text = 'Стоп'
            self.sound = SoundLoader.load('audio/gaiti.mp3')
            self.pos = 0
            self.button2.disabled = False
            self.sound.play()
        else:
            if self.button1.text == 'Стоп':
                self.l1.text = 'Нажмите Старт'
                self.button1.text = 'Старт'
                self.sound.unload()
                self.button2.disabled = True
                self.pos = 0

    def pause_resume(self, event):
        if self.button2.text == 'Пауза':
            self.button2.text = 'Продолжить'
            self.l1.text = 'Пауза'
            self.pos = self.sound.get_pos()
            print(self.pos)
            self.sound.stop()
        else:
            if self.button2.text == 'Продолжить':
                self.l1.text = 'Проигрывание'
                self.button2.text = 'Пауза'
                print(self.pos)
                self.sound.seek(self.pos)
                self.sound.play()

audioapp().run()