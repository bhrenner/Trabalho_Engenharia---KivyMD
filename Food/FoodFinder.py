from kivymd.app import MDApp, App
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout, MDFloatLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout, BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
import finder 

Window.size = (350,650)


class TelaLogin(Screen):
    def logado(self):
        MDApp.get_running_app().root.current = "logado"
    def deslogado(self):
        MDApp.get_running_app().root.current = "deslogado"
    ...

class TelaLogado (Screen):
    def voltar_login(self):
        MDApp.get_running_app().root.current = "tela_login"

class TelaDeslogado(Screen):
    def voltar_login(self):
        MDApp.get_running_app().root.current = "tela_login"
    def ir_resultado_des(self):
        MDApp.get_running_app().root.current = "resultado_des"

class TelaHome(Screen):
    resposta = False
    def abrir_card(self):
        self.add_widget(Resultado())
    def ir_resultado(self):
        MDApp.get_running_app().root.current = "resultado"
    

class Resultado(Screen):
    def voltar_logado(self):
        MDApp.get_running_app().root.current = "logado"

class ResultadoDes(Screen):
    def voltar_deslogado(self):
        MDApp.get_running_app().root.current = "deslogado"

class TelaFav(MDFloatLayout):
    pass


class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)
        

class TelaConta(FloatLayout): #classe herda floatlayout
    def abrir_card(self): #método para abrir o card
        self.add_widget(SenhaCard())
         

sm = ScreenManager()
sm.add_widget(Resultado(name='resultado'))
sm.add_widget(TelaLogin(name='tela_login'))
sm.add_widget(TelaHome(name='home'))

class MyApp(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.accent_palette = 'Red'
        return Builder.load_file('FoodFinder.kv')

    def presser(self, pressed, list_id):
        pressed.tertiary_text = f"You Pressed {list_id}"

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Excluir conta",
                text = "Tem certeza que deseja excluir sua conta?",
                buttons =[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release = self.close_dialog),
                    MDRectangleFlatButton(
                        text="Sim, excluir conta", text_color=self.theme_cls.primary_color, on_release = self.neat_dialog),
                    ],
                )
        self.dialog.open()

	# Click Cancel Button

    def close_dialog(self, obj):
		# Close alert box
        self.dialog.dismiss()
	
	# Click the Neat Button
    def neat_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()
        # Change label text
        self.root.ids.my_label.text = "Sim, excluir conta"
MyApp().run()

#criar uma variavel para receber um parametro e retornar para o metodo caso esteja logado ou não, para evitar criar outra tela de resultado