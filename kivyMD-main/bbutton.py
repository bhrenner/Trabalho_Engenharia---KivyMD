from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (400,750)


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('bbutton.kv')
	
	def presser(self):
		self.root.ids.my_label.text = "You Pressed It!!!"
	
MainApp().run()