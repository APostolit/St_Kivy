# Листинг 9.16
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    MDFloatingActionButtonSpeedDial:          
        # Свойства кнопок       
        data: app.data                    # иконки на кнопках стека
        root_button_anim: True            #повернуть корневую кнопку при нажатии
        #icon: "language-python"          #иконка на корневой кнопке
        #color_icon_root_button: 0,1,0,1  #цвет иконки корневой кнопки
        #bg_color_root_button: 1,0,0,1    #цвета фона иконки корневой кнопки 
        #color_icon_stack_button: 0,1,0,1 #цвет иконок кнопок стека
        #bg_color_stack_button: 1,0,0,1   #цвета фона иконок кнопок стека
        #label_text_color: 1,0,0,1        #цвета текста кнопок стека
        # вызов функций обработки событий нажатия кнопок
        on_open: app.open()   #нажата корневая кнопка
        on_close: app.close() #отжата корневая кнопка
'''
def press_bt(param):
    popup = Popup(title='Модальное окно',
                  content=Label(text='Нажата кнопка ' + param),
                  size_hint=(.8, .4))
    popup.open()

class MainApp(MDApp):
    data = {
        'Python': ['language-python',
                   "on_press", lambda x: press_bt('Python')],
        'Ruby': ['language-ruby',
                 "on_press", lambda x: press_bt('Ruby')],
        'JS': ['language-javascript',
               "on_press", lambda x: press_bt('JS')],
    }
    def build(self):
        return Builder.load_string(KV)
    def open(self):
        print("Корневая кнопка раскрыта")
    def close(self):
        print("Корневая кнопка закрыта")

MainApp().run()