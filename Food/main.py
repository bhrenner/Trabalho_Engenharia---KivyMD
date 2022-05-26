from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
import finder 

class ResultadosCard(MDCard):
   def __init__(self,name='',address='',photo='',**kwargs):
       super().__init__(**kwargs)
       self.ids.name.text = name
       self.ids.address.text = address
       self.ids.photo.source = photo

# Classes com as telas
class Resultados(Screen):
    ...
   
class Inicial(Screen):
    def busca(self):
        comida = self.ids.mealType.text
        local = self.ids.location.text

        resposta = []
        resposta.append(finder.findARestaurant(comida, local))
        resposta.append(finder.findARestaurant(comida, local))
        return resposta 

    def abrir_card(self,name,address,photo):
        self.add_widget(ResultadosCard(name=name, address=address, photo=photo))

class TelaLogin(Screen):
    ...

# Screen manager
sm = ScreenManager()
sm.add_widget(TelaLogin(name='tela_login'))
sm.add_widget(Inicial(name='inicial'))
sm.add_widget(Resultados(name='resultados'))

# Construção principal do app
class Myapp(MDApp):
    def build(self):
        return Builder.load_file('interface.kv')
    
# Inicia o aplicativo
Myapp().run()

