# Листинг 9.24
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "Вызов окна диалога"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''

class MainApp(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Сбросить настройки?",
                text="Это приведет к сбросу настроек по умолчанию",
                buttons=[MDFlatButton(text="НЕТ",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.closeDialog),
                         MDFlatButton(text="ДА",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.ok_Dialog,), ], )
        self.dialog.open()

    def ok_Dialog(self, inst):
        popup = Popup(title='Модальное окно',
                      content=Label(text='Нажата кнопка ДА'),
                      size_hint=(.8, .4))
        popup.open()
        self.dialog.dismiss()

    def closeDialog(self, inst):
        popup = Popup(title='Модальное окно',
                      content=Label(text='Нажата кнопка НЕТ'),
                      size_hint=(.8, .4))
        popup.open()
        self.dialog.dismiss()

MainApp().run()