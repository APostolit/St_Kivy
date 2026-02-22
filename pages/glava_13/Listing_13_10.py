# Листинг 13.10
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


# Приложение, запускающее видеофайл
class MyVideoApp(App):
    def build(self):
        self.player = VideoPlayer(source='video/My_video.mp4',
                                  state='play',
                                  options={'allow_stretch': True})
        return (self.player)


if __name__ == '__main__':
    MyVideoApp().run()