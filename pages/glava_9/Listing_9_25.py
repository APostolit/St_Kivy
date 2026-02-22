# Листинг 9.25
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem

KV = '''
<Item>
    ImageLeftWidget:
        source: root.source
MDFloatLayout:
    MDFlatButton:
        text: "Вызов окна диалога"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_simple_dialog()
'''

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

class MainApp(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Созданы следующие учетные записи",
                type="simple",
                items=[
                    Item(text="user01@gmail.com", source="images/Alex.jpg"),
                    Item(text="user02@gmail.com", source="images/Anna.jpg"),
                    Item(text="user02@gmail.com", source="images/Anna1.jpg"), ],
            )
        self.dialog.open()

MainApp().run()