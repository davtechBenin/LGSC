#Coding:utf-8
"""
	Définition de d'objet pour la simulation des balises html

	** Rest à définir comment importer un type de police depuis GoogleFont.**

	Lorsqu'on veut commencer la définition du style css d'un objet balise,
	on doit commencer par l'appel de méthode Begin_css()
"""
try:
	from .pycss.csssheet import cssSheet
	from .pycss.csscore import Css
except:
	from pycss.csssheet import cssSheet
	from pycss.csscore import Css

class balise(Css):
	def __init__(self,bal):
		Css.__init__(self)
		self.bal = bal
		self.attrs = str()
		self.Cont = str()
		self.attrs_dic = dict()
		self.span_names = list()
		self.All_css = str()
		self.el_list = list()

		self.css_n = False

	def Set_span_cont(self,cont,css_name,attrs_dic = dict()):
		sp = balise('span')
		sp.Set_cont(cont)
		sp.Set_attrs(attrs_dic)
		self.span_names+=css_name
		self.Set_cont(sp)

	def Set_cont(self,cont):
		self.Cont+=cont

	def Set_cont_obj(self,cont_obj):
		if type(cont_obj) == str:
			self.Cont+=cont
		else:
			self.el_list.append(cont_obj)
			self.Cont+=cont_obj.Run_html()

	def Modif_cont(self,cont):
		self.Cont = cont

	def Sup_cont(self):
		self.Cont = str()

	def Set_attr(self,attr,value):
		At = f'{attr}="{value}"'
		self.attrs_dic[attr] = value
		self.attrs += f' {At}'

	def Set_css_name(self,name):
		self.Set_attr('class',name)
		self.css_n = True

	def Get_css_name(self):
		return f".{self.Get_attr('class')}"

	def Set_Attrs(self,attrs_dic):
		for attr_name in attrs_dic:
			self.Set_attr(attr_name,attrs_dic[attr_name])

	def Get_attr(self,attr):
		at = self.attrs_dic.get(attr)
		return at

	def Set_name(self,name):
		self.Set_attr("name",name)

	def Set_id(self,Id):
		self.Set_attr("id",Id)

	def Set_style(self,style):
		"""
			style doit être un objet de définition de css
		"""
		if type(style) != str:
			style = style.Run_css_only()
		self.cont += style

		#self.Set_attr("style",style)

	def Set_type(self,Typ):
		self.Set_attr("type",Typ)

	def Set_href(self,href):
		self.Set_attr("href",href)

	def Align(self,side):
		"""
			side doit être soit:
				-> left
				-> right
				-> justify
				-> center
		"""
		self.Set_attr("align",side)

	def Run_html(self):
		self.Run_css_only()
		self.Set_attr("style",self.cont)
		Ct = f"""\n<{self.bal} {self.attrs}>\n{self.Cont}\n</{self.bal}>\n"""
		return Ct

	def Run_css(self,**kwarg):
		'''
			C'est la méthode utilisée pour céer une suite de chaine 
			composée des propriété css définie.

			Avec cette méthode, on donne une paramètre nommé avec le nom
			du style que nous voulons appliquer. 
		'''
		if self.css_n:
			select = self.Get_css_name()
		else:
			select = self.bal

		css_str = cssSheet.Run_css(select,**kwarg)
		return css_str

class div(balise):
	def __init__(self):
		balise.__init__(self,'div')

class baliseOrph(balise):
	def __init__(self,balise):
		balise.__init__(self,balise)

	def Run_html(self):
		self.Run_css_only()
		self.Set_attr("style",self.cont)
		Ct = f"""\n<{self.bal} {self.attrs}/>"""
		return Ct

class head(balise):
	def __init__(self,titre,rel = "stylesheet",charset = "utf-8"):
		balise.__init__(self,"head")
		self.titre = titre
		self.charset = charset
		self.rel = rel 
		self.Min()

	def Min(self):
		mi = f"""\t<meta charset="{self.charset}">\
\n\t<meta name="viewport" content="width=device-width" initial-scale="1">\
\n\t<title>{self.titre}</title>"""
		self.Cont = mi

	def Set_css_file(self,file_name):
		a = f'<link rel = "{self.rel}" type="text/css" href="{file_name}"'
		self.Cont += a

class header(balise):
	def __init__(self):
		balise.__init__(self,'header')

class section(balise):
	def __init__(self):
		balise.__init__(self,'section')

class footer(balise):
	def __init__(self):
		balise.__init__(self,'footer')

class nav(balise):
	def __init__(self):
		balise.__init__(self,'nav')

class main(balise):
	def __init__(self):
		balise.__init__(self,'main')

class aside(balise):
	def __init__(self):
		balise.__init__(self,'aside')

class uListe(balise):
	def __init__(self,Type = 'circle'):
		'''
			Type doit être soit circle, square ou disc
		'''
		balise.__init__(self,'ul')
		self.Set_type(Type)

	def Set_el(self,cont):
		El = f"<li>{cont}</li>"
		self.Set_cont(El)

class oListe(balise):
	def __init__(self,Type = '1'):
		'''
			Type doit être soit circle, square ou disc
		'''
		balise.__init__(self,'ol')
		self.Set_type(Type)

	def Set_el(self,cont):
		El = f"<li>{cont}</li>"
		self.Set_cont(El)

class anchor(balise):
	def __init__(self,href,desc):
		balise.__init__(self,'a')
		self.Set_href(href)
		self.Set_cont(desc)

	def Set_target(self,name = '_blank'):
		self.Set_attr('target',name)

class mail(anchor):
	def __init__(self,href,desc):
		href = f'mailto:{href}'
		anchor.__init__(self,href,desc)
		
class ancre(anchor):
	def __init__(self,name,desc,page_link=str()):
		name = f'{page_link}#{name}'
		anchor.__init__(self,href,desc)

class dic(balise):
	def __init__(self):
		balise.__init__(self,'dl')

	def Set_terme(self,terme,style_obj = None):
		Ter = balise("dt")
		Ter.Set_cont(terme)
		if style_obj:
			Ter.Set_style(style_obj)
		self.Set_cont(Ter.Run_html())

	def Set_def(self,defin,style_obj = None):
		Defin = balise("dd")
		Defin.Set_cont(defin)
		if style_obj:
			Defin.Set_style(style_obj)
		self.Set_cont(Defin.Run_html())

class body(balise):
	def __init__(self):
		balise.__init__(self,'body')

class p(balise):
	def __init__(self,cont):
		balise.__init__(self,"p")
		self.Modif_cont(cont)

class strong(balise):
	def __init__(self,cont):
		balise.__init__(self,"strong")

class mark(balise):
	def __init__(self,cont):
		balise.__init__(self,"mark")

class i(balise):
	def __init__(self):
		balise.__init__(self,'i')

class pre(balise):
	def __init__(self):
		balise.__init__(self,'pre')

class b(balise):
	def __init__(self):
		balise.__init__(self,'b')

class sub(balise):
	def __init__(self):
		balise.__init__(self,'sub')

class sup(balise):
	def __init__(self):
		balise.__init__(self,'sup')

class center(balise):
	def __init__(self):
		balise.__init__(self,'center')

class title1(balise):
	def __init__(self):
		balise.__init__(self,'h1')

class title2(balise):
	def __init__(self):
		balise.__init__(self,'h2')

class title3(balise):
	def __init__(self):
		balise.__init__(self,'h3')

class title4(balise):
	def __init__(self):
		balise.__init__(self,'h4')

class div(balise):
	def __init__(self):
		balise.__init__(self,'div')

class image(baliseOrph):
	def __init__(self,src,alt):
		balise.__init__(self,'img')
		self.Set_attr('src',src)
		self.Set_attr('alt',alt)

	def Set_title(self,title):
		self.Set_attr('title',title)

class img1ToImg2(anchor):
	def __init__(self,srcimg1,srcimg2,alt,title = "Click here"):
		img = image(srcimg1,alt)
		img.Set_title(title)
		anchor.__init__(self.srcimg2,img.Run())

class figure(balise):
	def __init__(self,El,legende):
		balise.__init__(self,'figure')
		self.Set_cont(El.Run())
		cp = f"<figcaption>{legende}</figcaption>"
		self.Set_cont(cp)

#Reste à revoir après la doc.
class table:
	def __init__(self):
		self = balise(self,'table')
		self.Begin_css()
		self.Add_css('border-collapse','collapse')
		self.Add_css('margin','auto')

		self.All_el = list()

	def Begin_row(self,style = None,attrs_dic = dict()):
		self.row = balise('tr')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def Begin_header(self,style = None,attrs_dic = dict()):
		self.head = balise('thead')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def End_header(self):
		self.Set_cont_obj(self.head)
		self.row = balise('thead')

	def Begin_footer(self,style = None,attrs_dic = dict()):
		self.foot = balise('tfoot')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def End_footer(self):
		self.Set_cont_obj(self.foot)
		self.row = balise('tfoot')

	def Begin_body(self,style = None,attrs_dic = dict()):
		self.body = balise('tbody')
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		self.row.Set_attrs(attrs_dic)

	def End_bodyer(self):
		self.Set_cont_obj(self.body)
		self.row = balise('tbody')

	def Set_data(self,cont,style = 'border: 1px solid black;',attrs_dic = dict(),bal='td'):
		data = balise(bal)
		if type(style) == dict:
			self.row.Set_mult_css(style)
		elif type(style) == str:
			self.row.Set_style(style)
		data.Set_attrs(attrs_dic)
		data.Set_cont_obj(cont)
		self.All_el.append()
		self.row.Set_cont_obj(data)

	def Set_header(self,cont,style = 'border: 1px solid black;',attrs_dic = dict()):
		self.Set_data(cont,style,attrs_dic,bal='th')

	def End_row(self):
		self.Set_cont_obj(self.row)
		self.row = balise('tr')

	def Set_title(self,cont,style_dic = None,caption_side = 'top'):
		self.title = balise('caption')
		self.title.Add_css('caption-side',caption_side)
		if style_dic:
			self.title.Add_mult_css(style_dic)
		self.Set_cont_obj(self.title)

class form(balise):
	def __init__(self,method='get',action=""):
		balise.__init__(self,'form')
		self.Set_attr('method',method)
		self.Set_attr('action',action)

	def Set_input(self,Type,name,attrs_dic=dict(),style_dic = dict()):
		Inp = baliseOrph('input')
		Inp.Set_attr('type',Type)
		Inp.Set_attr('name',name)
		Inp.Set_attrs(attrs_dic)
		Inp.Add_mult_css(style_dic)
		self.Set_cont_obj(Inp)

	def Set_label(self,cont,style_dic=dict()):
		pass
		

