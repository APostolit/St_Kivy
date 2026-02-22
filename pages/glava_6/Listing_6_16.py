# Листинг 6.16
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.window import Window
Window.size = (720, 350)

class MainApp(App):
    title = "Пример с видео проигрывателем"
    def build(self):
        player = VideoPlayer(
            source="video/Dictor.mp4",
            size_hint=(0.95, 0.95),
            options={'fit_mode': 'contain'}
        )
        player.state = 'play'
        player.options = {'eos': 'loop'}
        player.allow_stretch = True
        return player

MainApp().run()