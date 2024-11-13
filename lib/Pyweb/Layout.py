#Coding:utf-8
try:
	from .balises import *
except:
	from .balises import *

def transform(x,y):
	if x <= 1:
		x*=100
	if y <= 1:
		y*=100
	return (f"{x}%",f"{y}%")

class Layout(div):
	def __init__(self,style_obj = None):
		div.__init__(self)
		if style_obj:
			self.Set_style(style_obj)

		self.Y_Curent = 0 #Toujours en pourcentage

	def init_list(self):
		self.Y_Curent = 0

	def _set_wid(self,cont,size,pos,css_name = str(),Id = str(),
		attrs = dict(),custum_style = None,align = 'left',
		href = str(),typ = str(),bal_name = 'div',
		position = "absolute",display = 'inline',
		bg_color = (255,255,255),opacity = 1,
		combine_style = False):
	#
		size = transform(*size)
		pos = transform(*pos)
		Y = float(size[1][:-1])
		
		self.Y_Curent+=float(Y)

		This_bal = balise(bal_name)
		This_bal.Align(align)

	# Définition des attibuts html
		if type(cont) == str:
			This_bal.Set_cont(cont)
		else:
			This_bal.Set_cont_obj(cont)
		if css_name:
			This_bal.Set_css_name(css_name)
		if Id:
			This_bal.Set_id(Id)
		if attrs:
			This_bal.Set_Attrs(attrs)
		if custum_style:
			This_bal.Set_style(custum_style)
		if typ:
			This_bal.Set_type(typ)
		if href:
			This_bal.Set_href(href)

	#Défintion des styles css
		if not custum_style or combine_style:
			This_bal.Set_opacity(opacity)
			This_bal.Set_size(*size)
			This_bal.Set_position(position,
				{'left':pos[0],'top':pos[1]})
			This_bal.Set_bg_color(bg_color)
			This_bal.Set_display(display)

		return This_bal

	def add_wid(self,cont,size,pos,**wid_args):
		obj = self._set_wid(cont,size,**wid_args)
		self.Set_cont_obj(obj)

	def add_Text(self,text,size,pos,font_name = str(),
		font_size = 1,italic = None,bold = None,
		underline = False,text_color = (0,0,0),
		text_align = 'left',
		**wid_args):
	#
		bal = 'p'
		if 'bal_name' in wid_args:
			bal = wid_args["bal_name"]
			del wid_args["bal_name"]
		Text_obj = self._set_wid(text,size,pos,bal_name = bal,
			**wid_args)
		combine_style = wid_args.get("combine_style",False)
		custum_style = wid_args.get('custum_style',None)
		if not custum_style or combine_style:
			Text_obj.Set_font_size(font_size)
			Text_obj.Set_font_family(font_name)
			Text_obj.Set_underline(underline)
			Text_obj.Set_text_align(text_align)
			if bold:
				Text_obj.Set_font_weight(500)
			if italic:
				Text_obj.Set_font_style('italic')
			Text_obj.Set_text_color(text_color)
		self.Set_cont_obj(Text_obj)

	def add_button(self,text,size,pos,action_fonc,
		font_name = str(),font_size = 1,italic = None,
		bold = None,underline = False,text_color = (0,0,0),
		text_align = 'left',**wid_args):
	#
		if 'bal_name' in wid_args:
			del wid_args["bal_name"]
		But_obj = self._set_wid(text,size,pos,bal_name = 'button',
			**wid_args)
		combine_style = wid_args.get("combine_style",False)
		custum_style = wid_args.get('custum_style',None)
		if not custum_style or combine_style:
			But_obj.Set_font_size(font_size)
			But_obj.Set_font_family(font_name)
			But_obj.Set_underline(underline)
			But_obj.Set_text_align(text_align)
			if bold:
				But_obj.Set_font_weight(500)
			if italic:
				But_obj.Set_font_style('italic')
			But_obj.Set_text_color(text_color)
		But_obj.Set_attr('action',action_fonc)

		self.Set_cont_obj(But_obj)

	def add_image(self,url,alt,size,pos,title,):
		img_obj = image(url,alt)
		size = transform(*size)
		pos = transform(*pos)
		img_obj.Set_title(title)
		img_obj.Set_size(*size)
		img_obj.Set_position("absolute",{'top':pos[1],
			'left':pos[0]})
		self.Set_cont_obj(img_obj)
		Y = float(size[1][:-1])
		self.Y_Curent+=float(Y)

	def add_table(self,table_obj):
		# Doit être définie directement avec l'objet CSS
		self.Set_cont_obj(table_obj)

	def add_form(self,form_obj):
		# Pareil pour le table
		self.Set_cont_obj(form_obj)

	def add_title(self,text,size,pos,bal_name = "h2",**text_args):
		self.add_Text(text,size,pos,bal_name = bal_name,
			**text_args)

	def add_link(self,text,url,size,pos,
		bg_color = (200,200,200),underline = False,
		text_color = (0,0,0),text_size = .85,
		new_wind =False):
		A = anchor(url,text)
		A.Set_size(*size)
		P = transform(*pos)
		A.Set_position('absolute',{'left':P[0],"top":P[1]})
		if bg_color:
			A.Set_bg_color(bg_color)
		A.Set_underline(underline)
		A.Set_text_color(text_color)
		A.Set_font_size(text_size)

		self.Set_cont_obj(A)










		


