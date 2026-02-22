# Листинг 6.14
from kivy.app import App
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.clearcolor = '#55555555'

class DemoApp(App):
    def build(self):
        lo = BoxLayout(orientation='vertical')

        self.tv = TreeView(root_options={
            'text': 'Учебные курсы',
            'font_size': 20})
        self.n1 = self.tv.add_node(TreeViewLabel(text='Гуманитарные'))
        self.n2 = self.tv.add_node(TreeViewLabel(text='Экономика'))
        self.n3 = self.tv.add_node(TreeViewLabel(text='Программирование'))

        self.n4 = self.tv.add_node(
            TreeViewLabel(text='Социология'), self.n1)
        self.n5 = self.tv.add_node(
            TreeViewLabel(text='История'), self.n1)
        self.n6 = self.tv.add_node(
            TreeViewLabel(text='Психология'), self.n1)

        self.n7 = self.tv.add_node(
            TreeViewLabel(text='В торговле'), self.n2)
        self.n8 = self.tv.add_node(
            TreeViewLabel(text='На транспорте'), self.n2)
        self.n9 = self.tv.add_node(
            TreeViewLabel(text='В геологии'), self.n2)

        self.n10 = self.tv.add_node(
            TreeViewLabel(text='Настольные приложения'), self.n3)
        self.n11 = self.tv.add_node(
            TreeViewLabel(text='WEB приложения'), self.n3)
        self.n12 = self.tv.add_node(
            TreeViewLabel(text='Мобильные приложения'), self.n3)

        lo.add_widget(self.tv)
        return lo

DemoApp().run()