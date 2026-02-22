# Листинг 4.18
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker

class ColorPickApp(App):
    def build(self):
        # Метка
        self.layout = GridLayout(cols=1, padding=10)
        self.l1 = Label(
            text='Текущий цвет',
            font_size=48, color=[.8, .6, .4, 1]
        )
        self.layout.add_widget(self.l1)
        # Кнопка открытия виджета ColorPicker
        self.button = Button(text="Открыть ColorPicker")
        self.layout.add_widget(self.button)
        self.button.bind(on_press=self.onButtonPress)
        return self.layout

    # Обработка события кнопки открытия ColorPicker
    def onButtonPress(self, button):
        layout = GridLayout(cols=1, padding=10)
        self.clr = ColorPicker()
        closeButton = Button(text="Выбрать цвет",
                             size_hint=(.2, .2))
        layout.add_widget(self.clr)
        layout.add_widget(closeButton)
        self.popup = Popup(
            title='Виджет ColorPicker', content=layout,
            auto_dismiss=False)
        self.popup.open()
        closeButton.bind(on_press=self.on_close)

    # Обработка события кнопки закрытия ColorPicker
    def on_close(self, event):
        self.l1.color = self.clr.hex_color
        self.popup.dismiss()

ColorPickApp().run()