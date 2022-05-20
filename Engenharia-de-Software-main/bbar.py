from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.utils.fitimage import FitImage
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip

class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass
Window.size = (375,625)


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Orange"
		self.theme_cls.primary_hue = "600"
		return Builder.load_file('bbar.kv')
		
	def presser(self, pressed, list_id):
		pressed.tertiary_text = f"You Pressed {list_id}"
MainApp().run()	


'''#jbsidis
import os
from kivy.clock import Clock

class Example(MDApp):
	def nn(self):
			self.file_manager = MDFileManager()
			self.file_manager.exit_manager=self.exit_manager
			self.file_manager.select_path=self.select_path  
	## This error is bacause in your own example, the ID of the widgets are different or they must
	## be accessed in a different way
	##        self.root.ids.n1.disabled=False
	##   File "kivy/properties.pyx", line 864, in kivy.properties.ObservableDict.__getattr__
	## AttributeError: 'super' object has no attribute '__getattr__'
			##the id "n1" doesnot exists in the kivy Lang section, so we should specify which one is it
			##the id "edit_profile_pic" does exists in the kivy Lang section
			#BAD ===== self.root.ids.n1.disabled=False
			#GOOD
			self.root.ids.edit_profile_pic.disabled=False
			self.root.ids.edit_cover_pic.disabled=False
			
	def chpic(self,new):
		if os.path.isfile(new)==True:
			if self.image_is_profile_or_cover=="cover":
					self.root.ids.cover_pic.source=new
					print("The picture on 'id: cover_pic' was changed to:",self.root.ids.cover_pic.source)
			if self.image_is_profile_or_cover=="profile":
					self.root.ids.profile_pic.source=new
					print("The picture on 'id: profile_pic' was changed to:",self.root.ids.profile_pic.source)
	def file_manager_open_for_profile(self):
			self.image_is_profile_or_cover="profile"
			self.file_manager.show('/')  # output manager to the screen
			self.manager_open = True
'''
