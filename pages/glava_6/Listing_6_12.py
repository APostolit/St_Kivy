# Листинг 6.12
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors.touchripple import TouchRippleBehavior
from kivy.core.window import Window
Window.clearcolor = '#19a8ffff'

class RippleLabel(TouchRippleBehavior, GridLayout):
   def on_touch_down(self, touch):
      collide_point = self.collide_point(touch.x, touch.y)
      if collide_point:
         touch.grab(self)
         self.ripple_duration_in=3
         self.ripple_show(touch)
         return True
      return False

   def on_touch_up(self, touch):
      if touch.grab_current is self:
         touch.ungrab(self)
         self.ripple_duration_out=3
         self.ripple_fade()
         return True
      return False

class MyRippleApp(App):
   def build(self):
      return RippleLabel(cols=1)

MyRippleApp().run()