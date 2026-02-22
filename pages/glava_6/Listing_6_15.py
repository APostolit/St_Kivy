# Листинг 6.15
from kivy.app import App
from kivy.uix.video import Video
from kivy.core.window import Window
Window.size = (720,400)

class MainApp(App):
   title = "Simple Video"
   def build(self):
      player = Video(source = "video/My_video.mp4",
         size_hint = (1,1),
         options={'fit_mode': 'contain'})
      player.state = 'play'
      player.options = {'eos': 'loop'}
      player.allow_stretch=True
      return player

MainApp().run()