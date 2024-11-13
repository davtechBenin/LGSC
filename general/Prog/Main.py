#Coding:utf-8
"""
	Module de création de la page d'accueil de la 
	surface générale
"""
from lib.Pyweb.web_page import Web_P
from lib.Pyweb.Layout import Layout
from lib.Pyweb import balises as bl
from lib.Pyweb.pyhtml import form
Css = bl.Css
from . import TEXT
from color import *
import urllib
from . import CSS
from .Accueil import Acc_main

class Ac_Main(Web_P):
	def __init__(self,request):
		Web_P.__init__(self,titre = "Accueil")

		self.req_hand(request)

		self.add_balise_obj(Main(self))

	def req_hand(self,request):
		self.Curent_ret = request.GET.get("request",str())

class Main(Layout):
	def __init__(self,parent):
		Layout.__init__(self,style_obj = CSS.Main_Css)

		self.Present = Present(parent)
		self.Connexion = Connexion(parent)
		self.Services = Services(parent)
		self.Services_T = Services_T(parent)

		self.Set_cont_obj(self.Present)
		self.Set_cont_obj(self.Connexion)
		self.Set_cont_obj(self.Services)
		self.Set_cont_obj(self.Services_T)

class Present(Layout):
	def __init__(self,parent):
		Layout.__init__(self,style_obj = CSS.Present_Css)

		self.CSS()
		self.Render()

	def CSS(self):
		self.log_css = Css()
		self.log_css.Set_size(.3,.4)
		self.log_css.Set_position("absolute",{"left":"2.5%",'top':"5%"})

		self.Descip_css = Css()
		#self.Descip_css.Set_display("inline")
		self.Descip_css.Set_size(.6,.3)
		self.Descip_css.Set_position("absolute",{"left":"35%",'top':"10%"})


		self.Object_css = Css()
		self.Object_css.Set_size(.96,.5)
		self.Object_css.Set_position("absolute",{"left":'2.5%','top':"45%"})
		
	def Render(self):
		logo = bl.image("/static/general/logo.jpg","logo Rupin")
		logo.Set_style(self.log_css)

		Descip = Layout()
		Descip.Set_style(self.Descip_css)
		Descip.add_title('Le Rupin',(.8,.2),(.1,0),
			bg_color = None,text_color = MAIN_COL)
		Descip.add_Text("Bref description",(.8,.8),(.1,.22),bg_color = None
			,font_size = .9,text_color = MAIN_COL)

		Object = Layout()
		Object.Set_style(self.Object_css)
		Object.add_title('Notre objectif',(.8,.1),(.1,0),
			bg_color = None,text_color = TEXT_COL2)
		Object.add_Text("L'objectif de votre organisation",(.8,.8),(.1,.15)
			,bg_color = None,font_size = .9
			,text_color = TEXT_COL2)

		self.Set_cont_obj(logo)
		self.Set_cont_obj(Descip)
		self.Set_cont_obj(Object)

class Connexion(Layout):
	def __init__(self,parent):
		Layout.__init__(self,style_obj = CSS.Connexion_Css)
		self.Foreign_surf()

	def Foreign_surf(self):
		self.add_Text(TEXT.Con,(1,.3),(0,0),
			text_color = TEXT_COL1,text_align = 'center',
			font_size = .86)

		F_css = Css()
		F_css.Set_size(1,.4)
		F_css.Set_position("absolute",{"left":'0%','top':"30%"})

		inp_css = Css()
		inp_css.Set_size(.55,.2)
		#inp_css.Set_bg_color(MAIN_COL)
		inp_css.Set_position("absolute",{"left":'32%','top':"0%"})

		lab_css = Css()
		lab_css.Set_size(.3,.15)
		lab_css.Set_position("absolute",{"left":'0%','top':"5%"})
		lab_css.Set_display("block")
		lab_css.Set_text_align('right')
		lab_css.Set_font_size(.8)

		self.F = form.form()
		self.F.Set_style(F_css)
		self.F.Set_email_input(TEXT.EMAIL,inp_style = inp_css,
			lab_style = lab_css)
		lab_css = Css()
		lab_css.Set_size(.3,.15)
		lab_css.Set_display("block")
		lab_css.Set_text_align('right')
		lab_css.Set_font_size(.8)
		lab_css.Set_position("absolute",{"left":'0%','top':"35%"})

		inp_css = Css()
		inp_css.Set_size(.55,.2)
		#inp_css.Set_bg_color(MAIN_COL)
		inp_css.Set_position("absolute",{"left":'32%','top':"30%"})
		self.F.Set_password_input(TEXT.PASS,inp_style = inp_css,
			lab_style = lab_css)

		inp_css = Css()
		inp_css.Set_size(.7,.23)

		inp_css.Set_position("absolute",{"left":'15%','top':"65%"})
		
		self.F.End_form(submit_name = TEXT.VALIDER,
			Submit_style = inp_css)

		self.Set_cont_obj(self.F)

		Conn_Css = Css()
		Conn_Css.Set_size(.7,.06)
		Conn_Css.Set_text_color(TEXT_COL3)
		Conn_Css.Set_font_size(.8)
		Conn_Css.Set_underline(False)
		Conn_Css.Set_text_align("center")
		Conn_Css.Set_position('absolute',{"left":"15%",'top':"73%"})

		L = urllib.parse.urlencode({"request":"SAVE_NEW"})
		L = "?"+L
		A = bl.anchor(L,"Pas encode de compte?")
		A.Set_style(Conn_Css)

		self.Set_cont_obj(A)

class Services(Layout):
	def __init__(self,parent):
		Layout.__init__(self,style_obj = CSS.Services_Css)

		self.add_Text(TEXT.SERVICE,(.7,.1),(.15,0),
			text_color = TEXT_COL4,font_size = .9,
			)
		dic = TEXT.Serv_dic
		X = 2.5
		for name,img in dic.items():
			self.add_service(X,name,img)
			X+= 22.5

	def add_service(self,X,titre,image):
		Cont_css = Css()
		Cont_css.Set_size(.2,.7)
		Cont_css.Set_position("absolute",{'left':f'{X}%',"top":'22.5%'})
		Cont_css.Set_bg_color(OPTION_COL)
		Cont_css.Set_display("block")

		bg_img_css = Css()
		bg_img_css.Set_size(1,1)
		bg_img_css.Set_position("absolute",{"left":'0','top':'0'})

		bg_img = bl.image(image,'img')
		bg_img.Set_style(bg_img_css)


		log_css = Css()
		log_css.Set_size(.15,.3)
		log_css.Set_position("absolute",{"left":'2.5%','top':'5%'})

		log = bl.image("/static/general/logo.jpg","")
		log.Set_style(log_css)

		
		T_css = Css()
		T_css.Set_size(1,.48)
		T_css.Set_position("absolute",{"left":'0','top':'40%'})
		T_css.Set_opacity(.7)
		T_css.Set_bg_color(OPTION_COL)
		T_css.Set_text_color(TEXT_COL2)
		T_css.Set_text_align("center")
		
		T = bl.p(titre)
		T.Set_style(T_css)

		L = urllib.parse.urlencode({"request":f"Service {titre}"})
		L = "?"+L

		Cont = bl.anchor(L,"")
		Cont.Set_style(Cont_css)
		Cont.Set_cont_obj(bg_img)
		Cont.Set_cont_obj(log)
		Cont.Set_cont_obj(T)

		self.Set_cont_obj(Cont)

class Services_T(Layout):
	def __init__(self,parent):
		Layout.__init__(self,style_obj = CSS.Services_T_Css)

		self.add_Text(TEXT.Cont_text,(1,.2),(0,0),
			text_color = TEXT_COL3,font_size = .8,
			underline = True,text_align = 'center',
			bg_color = None)

		Y = 15
		X1 = 0
		X2 = 30
		for key,num in TEXT.Contact_dict.items():
			self.add_Text(key,(X2,.2),(X1,Y),
				text_color = TEXT_COL4,font_size = .8,
				bg_color = None)
			self.add_Text(num,(70,.2),(X2,Y),
				text_color = TEXT_COL1,font_size = .9,
				bg_color = None)
			Y += 20

