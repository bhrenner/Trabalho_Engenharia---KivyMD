from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (400,750)


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Orange"
		self.theme_cls.primary_hue = "600"
		return Builder.load_file('bbar.kv')
		
	def presser(self, pressed, list_id):
		pressed.tertiary_text = f"You Pressed {list_id}"
	
MainApp().run()