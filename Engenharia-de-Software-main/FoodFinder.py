from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout, MDFloatLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

Window.size = (375,650)

class TelaFav(MDFloatLayout):
    ...

class TelaHome(MDFloatLayout):
	...

class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class TelaConta(FloatLayout): #classe herda floatlayout
    def abrir_card(self): #método para abrir o card
        self.add_widget(SenhaCard())

class MyApp(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.accent_palette = 'Red'
        return Builder.load_file('FoodFinder.kv')

    def show_alert_dialog(self):
            if not self.dialog:
                self.dialog = MDDialog(
                    title = "Excluir conta",
                    text = "Tem certeza que deseja excluir sua conta?",
                    buttons =[
                        MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                            ),
                        MDRectangleFlatButton(
                            text="Sim, excluir conta", text_color=self.theme_cls.primary_color, on_release = self.neat_dialog
                            ),
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

    def presser(self, pressed, list_id):
        pressed.tertiary_text = f"You Pressed {list_id}"
	
MyApp().run()