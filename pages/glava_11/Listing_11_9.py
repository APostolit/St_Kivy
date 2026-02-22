# Листинг 11.9
from typing import Union
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDColorPicker

KV = '''
MDScreen:
    MDTopAppBar:
        id: toolbar
        title: "Color Picker"
        pos_hint: {"top": 1}

    MDRaisedButton:
        text: "Открыть PICKER"
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: toolbar.md_bg_color
        on_release: app.open_color_picker()
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    # Открыть MDColorPicker
    def open_color_picker(self):
        color_picker = MDColorPicker(size_hint=(0.45, 0.85))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            on_release=self.get_selected_color,)

    # Обновить MDTopAppBar выбранным цветом
    def update_color(self, color: list) -> None:
        self.root.ids.toolbar.md_bg_color = color

    # Вызывается при нажатии на кнопку Select
    def get_selected_color(self,
                           instance_color_picker: MDColorPicker,
                           type_color: str,
                           selected_color: Union[list, str], ):
        # обновить панель инструментов выбранным цветом
        self.update_color(selected_color[:-1] + [1])
        # Создать из списка текст
        str_color = ', '.join(map(str, selected_color))
        self.show_dialog(str_color)

    # Вызывается при нажатии на градиентное изображение
    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        # Создать из списка текст
        str_color = ', '.join(map(str, color))
        # self.show_dialog(str_color)

    # Показать выбранный цвет
    def show_dialog(self, text_item):
        dialog = MDDialog(text='Выбран цвет: ' + text_item)
        dialog.open()

MyApp().run()