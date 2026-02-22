# Листинг 4.2
from kivy.app import App
from kivy.lang import Builder

KV = '''
Accordion:    
    orientation: 'vertical'      
    AccordionItem:
        title: "Слайдер"          
        title: 'Пица "Маргарита"'
        Image:
            source: 'images/Margaritta.jpg'
    AccordionItem:
        title: 'Пица "Маринара"'
        Image:
            source: 'images/Marinara.jpg'
    AccordionItem:
        title: 'Пица "Наполетана"'
        Image:
            source: 'images/Napoletana.jpg'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()