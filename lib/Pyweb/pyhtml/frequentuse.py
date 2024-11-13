#Coding:utf-8
from .htmlcore import balise
"""
	Cette classe regorge tous les balises HTML utiliser lors de
	la création d'une page html
"""

class head(balise):
	def __init__(self,titre,rel = "stylesheet",charset = "utf-8"):
		balise.__init__(self,"head")
		self.titre = titre
		self.charset = charset
		self.rel = rel 
		self.Min()

	def Min(self):
		mi = f"""
	<meta charset="{charset}">
	<meta name = "viewport" content = "width=device-width", initial-scale=1.0">
	<title>"{self.titre}"</title>
		"""
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

	def Set_terme(self,terme):
		Ter = f"<dt>{terme}</dt>"
		self.Set_cont(Ter)

	def Set_def(self,defin):
		de = f'<dd>{defin}</dd>'
		self.Set_cont(de)

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
		self.Set_Attr('src',src)
		self.Set_Attr('alt',alt)

	def Set_title(self,title):
		self.Set_Attr('title',title)

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

class progress(balise):
	def __init__(self):
		balise.__init__(self,'progress')

class time(balise):
	def __init__(self):
		balise.__init__(self,'time')

class kbd(balise):
	def __init__(self):
		balise.__init__(self,'kbd')

class address(balise):
	def __init__(self):
		balise.__init__(self,'address')
