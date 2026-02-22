# Листинг 6.2
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
Window.clearcolor = '#19a8ffff'

KV = '''
Widget
	BoxLayout:
		orientation: "vertical"
		size: root.width, root.height
		Splitter:
			sizable_from: 'bottom'
			Button:
				text: "Кнопка верхняя"
				font_size: 16
		Label:
			text: "Это текстовая метка"
			font_size: 16
		Splitter:
			sizable_from: 'top'
			Button:
				text: "Кнопка средняя"
				font_size: 16
		GridLayout:
			cols:2
			Button: 
				text: "Кнопка левая"
				font_size: 16
			Splitter:
				sizable_from: 'left'
				Button: 
					text: "Кнопка правая"
					font_size: 16
'''
class SplitterApp(App):
    def build(self):
        return Builder.load_string(KV)

SplitterApp().run()