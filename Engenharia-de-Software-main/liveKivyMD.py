from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard

from kivy.core.window import Window
Window.size = (375,625)
'''
    - Widgets:  Exitem widgets de layout que são feitos para posicionamento
    e widgets de interface que tem interação com alguma pessoa
'''
KV = '''
FloatLayout:
    MDRaisedButton:
        text: "Clique"
'''

class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class ExContaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class TelaConta(FloatLayout): #classe herda floatlayout
    def abrir_card(self): #método para abrir o card
        self.add_widget(SenhaCard())
    def excluirconta(self):
        self.add_widget(ExContaCard())

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.accent_palette = 'Red'
        #self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('liveKivyMD.kv')

MyApp().run()