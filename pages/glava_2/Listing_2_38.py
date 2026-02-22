# Листинг 2.38
from kivy.app import App
from kivy.uix.video import Video

class MainApp(App):
    def build(self):
        video = Video(source="video/My_video.mp4", play=True)
        return video

MainApp().run()