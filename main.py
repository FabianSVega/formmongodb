#Fabian Segura
# Librerias de  KIVY
import imp
from pymongo                    import MongoClient
import os
import time
import logging
import json
from pymongo                    import MongoClient
from PIL 						import ImageFont
from kivy.clock					import Clock
from kivy.lang					import Builder
from kivymd.app					import MDApp
from kivymd 					import images_path
from kivymd.uix.snackbar		import Snackbar
from kivy.uix.screenmanager 	import ScreenManager, Screen
from kivy.core.window 			import Window
from kivy.uix.image 			import Image as imagen
from kivymd.uix.button 			import MDFillRoundFlatButton
from kivymd.uix.card			import MDCard
from kivymd.uix.label			import MDLabel
from kivy.uix.image				import AsyncImage
from kivymd.uix.button			import MDFlatButton, MDRectangleFlatButton, MDRaisedButton,MDRoundFlatButton
from kivymd.uix.dialog			import MDDialog
from kivy.uix.boxlayout			import BoxLayout
from kivy.properties 			import StringProperty
from kivy.uix.button			import Button
from kivy.uix.video				import Video
from kivymd.uix.button          import MDFloatingActionButtonSpeedDial
from kivymd.uix.menu            import MDDropdownMenu
from kivymd.uix.floatlayout     import MDFloatLayout
from kivymd.uix.tab             import MDTabsBase

#tamaño de pantalla
Window.fullscreen = True
Window.clearcolor = (1, 1, 1, 1)
# Librerias funcionales

class ShowcaseScreen(Screen):
    
    def add_widget(self, *args, **kwargs):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args, **kwargs)
        return super(ShowcaseScreen, self).add_widget(*args, **kwargs)
class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Content(BoxLayout):
    
    pass
#time.clock_settime
class MainApp(MDApp):
	#varibles de estado de manejo
    screens	= {}
    dialog = None
    datas       ={'Clientes': 'account-group','Personas': 'nature-people','token': 'card-account-details','sities':'city-variant-outline',}
    baseskv     ={'Save': 'content-save-all','Delete': 'delete','Help': 'help-circle-outline','contact':'phone-classic','check your form':'check-decagram', }
    tokenkv     ={'Save': 'content-save-all','Delete': 'delete','Help': 'help-circle-outline','contact':'phone-classic','check your form':'check-decagram', }
    siteskv     ={'Save': 'content-save-all','Delete': 'delete','Help': 'help-circle-outline','contact':'phone-classic','check your form':'check-decagram', }
    peoplekv    ={'Save': 'content-save-all','Delete': 'delete','Help': 'help-circle-outline','contact':'phone-classic','check your form':'check-decagram', }

    def callback(self, instance):
        if instance.icon=='account-group':
            self.go_screen('base')
        elif instance.icon== 'nature-people':
            self.go_screen('people')
        elif instance.icon==  'card-account-details':
            self.go_screen('token')
        elif instance.icon=='city-variant-outline':
            self.go_screen('sites')
    def form(self,instance):
        if instance.icon=='content-save-all':
            print("content-save-all")
        elif instance.icon== 'delete':
            print("delete")
            
        elif instance.icon==  'help-circle-outline':
            print('help-circle-outline')
        elif instance.icon=='phone-classic':
           print('phone')
        elif instance.icon == 'check-decagram':
            print('check')
        
    def build(self):
		# ACTIVADOR DE CLASES
		# ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray'] 
        self.theme_cls.primary_palette	= "Teal"
		# Funciones paralelas
        Clock.schedule_interval(self._update_clock, 1)
        Clock.schedule_interval(self._update_clock, 1 / 60.)
        items = [
            {
                "viewclass": "OneLineListItem",
                "height": (60),
                "widht":(100),
                "text": f"Item {i}",
            }
            for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=items,
            
        )
        
        self.settings()
        self.createdbase()
        self.principal()

    
    def go_screen(self, screenname):	self.root.ids.sm.switch_to(self.load_screen(screenname), direction	= 'left', duration=.07)  #Ir a la vista
    
            
    def load_screen(self, screenname):
        self.view	= screenname
        if self.screens.get(screenname) is not None:	return self.screens.get(screenname)
        if os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/' + screenname.replace(" ", "") + '.kv'):
                print(os.path.dirname(os.path.realpath(__file__))+'/' + screenname.replace(" ", "") + '.kv')
                screen	= Builder.load_file(os.path.dirname(os.path.realpath(__file__))+'/' + screenname.replace(" ", "") + '.kv')
                print(os.path.dirname(os.path.realpath(__file__))+'/' + screenname.replace(" ", "") + '.kv')
        else:												screen	= Builder.load_string(f'''
																						
Screen:
	name: '{screenname} Not Defined'

	MDBoxLayout:
		orientation: 'vertical'
		MDLabel:
			text: "Screen {screenname} Not Defined"
			font_size: 40
			halign: 'center'
			size_hint_y: None
			''')
        print("print screen")
        self.screens[screenname]	= screen
        print(self.screens[screenname])
        return screen


    def _update_clock(self, dt):	self.root.ids["date"].text	= time.strftime('%Y-%m-%d %H:%M:%S')		 #Actualiza el reloj
	
    def settings(self):
        logging.info("--------------------------------------------------------------------> settings")
        dir_settings	= os.path.dirname(os.path.realpath(__file__))+'/data/'
        file_settings	= dir_settings + 'Productos.json'
        if os.path.exists(dir_settings):
            if os.path.exists(file_settings):
                with open(file_settings ) as file:
                    settings	= json.load(file)
                    logging.info(json.dumps(settings, indent	= 6))
                    self.config_catalogo		= settings['catalogo']
                    self.config_cameras		= settings['cameras']
                    self.status_settings	= True
                    print(self.config_cameras)
            else:	logging.error("SETTINGS NO FOUND")
        else:	logging.error("DIRECTORY NOT FOUND")
        logging.info("-------------------------------------------------------------------------------------< settings")
    def logger(self):
		#self.root.current = 'user'  # just switch to the other Screen
		#self.root.ids.hello_user.text = f"Hello {self.root.ids.username.text}"
        self.go_screen('principal')

    def logout(self):
        self.root.current = 'login'  # switch back to the login Screen
    def createdbase(self):
        client = MongoClient('localhost')
        self.db= client['testprueba']
        self.basededatos =self.db['products']
    def callbackm(self, button):
        self.menu.caller = button
        self.menu.open()
        
    def enterthis(self):
        name=self.screens['base'].ids.username.text
        print(name)
    def base(self):
        username    = self.screens['base'].ids.username.text
        email       = self.screens['base'].ids.email.text
        numberp     = self.screens['base'].ids.numberp.text
        nit         = self.screens['base'].ids.nit.text
        idd         = self.screens['base'].ids.idd.text
        city        = self.screens['base'].ids.city.text
        address     = self.screens['base'].ids.address.text
        postal      = self.screens['base'].ids.postal.text  
        self.basededatos.insert_one({"name":str(username),
                                     "email":str(email),
                                     "numberp":str(numberp),
                                     "nit":str(nit),
                                     "idd":str(idd),
                                     "city":str(city),
                                     "address":str(address),
                                     "postal":str(postal) })
        print(self.basededatos.find_one({"name":"fabian"}))
         
        
    def people(self):
        username    = self.screens['people'].ids.username.text
        email       = self.screens['people'].ids.email.text
        typed       = self.screens['people'].ids.typed.text
        self.basededatos.insert_one({"name":str(username),
                                     "email":str(email),
                                     "typed":str(typed)})
        print(self.basededatos.find_one({"name":"fabian"}))
        
        
    def sites(self): 
        username    = self.screens['sites'].ids.username.text
        id          = self.screens['sites'].ids.id.text
        country     = self.screens['sites'].ids.country.text
        city        = self.screens['sites'].ids.city.text
        postal      = self.screens['sites'].ids.postal.text
        self.basededatos.insert_one({"name":str(username),
                                      "country":str(country),
                                      "city":str(city),
                                      "postal":str(postal)})
        
        print(self.basededatos.find_one({"name":"fabian"}))
    
    def token(self): 
        username    = self.screens['token'].ids.username.text
        peopleid    = self.screens['token'].ids.peopleid.text
        tokentype   = self.screens['token'].ids.tokentype.text
        tokendata   = self.screens['token'].ids.tokendata.text
        self.basededatos.insert_one({"name":str(username),
                                     "peopleid":str(peopleid),
                                     "tokentype":str(tokentype),
                                     "tokendate":(tokendata)
                                      })
        print(self.basededatos.find_one({"name":"fabian"}))
        
        print(self.tokenb)
    
    def principal(self):
        self.go_screen('principal')
        font = ImageFont.load_default()
        self.root.ids.info.text	= " Bienvenido al sistema de Logeo "
        #Snackbar(text="PPA FUERA DE SERVICIO").open()

	
	
if __name__== "__main__":	MainApp().run()

