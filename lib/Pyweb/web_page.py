#Coding:utf-8
"""
	Cet module consiste à la définition d'un objet général
	pour la gestion effective d'une page html. Il met en relation
	tous les autre classe préalablement définie.
"""
try:
	from .import balises
	from .pycss.csscore import Css
except ModuleNotFoundError:
	import balises
	from pycss.csscore import Css

import webbrowser

class Web_P():
	def __init__(self,titre = "PyWeb",css_file = str()):
		self.HTML_page = "<!DOCTYPE html>\n<html>\n"
		head = balises.head(titre)
		self.temp = str()
		if css_file:
			head.Set_css_file(css_file)
		self.HTML_page += head.Run_html()

		self.Body = balises.body()

	def add_balise(self,name,cont,css_name = str(),Id = str(),
		attrs = dict(),custum_style = None,align = 'left',
		href = str(),construct_css = False,typ = str()):
	#
		"""
			Cette méthode se présente comme la méthode principale 
			pour l'ajout des éléments dans notre page HTML/CSS.
			Les valeurs prises correspondent au méthode de la
			classe de base balise.

			Les arguments restera le même pour tous les autres
			éléments de la page à quelque spécificité près
		"""
		ret_css = str()

		This_bal = balises.balise(name)
		This_bal.Align(align)
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
		
		self.Body.Set_cont_obj(This_bal)
		return ret_css

	def add_balise_obj(self,bal_obj):
		"""
			En ce qui concerne cette méthode, in s'agit d'une
			définition totale de balise html puit une intégration
			dans le corps de la page.
		"""
		self.Body.Set_cont_obj(bal_obj)

	def End_page(self):
		body = self.Body.Run_html()
		self.HTML_page+=body
		self.HTML_page+='\n</html>'

	def Run(self):
		self.End_page()
		return self.HTML_page

	def create_page(self,name):
		from pathlib import Path as ph 
		work_dir = ph.cwd()
		dirs = name.split("/")
		if len(dirs)>1:
			for di in dirs[:-1]:
				work_dir = work_dir.joinpath(di)
				if not work_dir.exists():
					work_dir.mkdir()
		if ".html" not in name:
			name = name+'.html'
		with open(name,'w') as fic:
			fic.write(self.temp)
			fic.write(self.Run())
		
		return ph.cwd()/name

	def add_temp(self,temp):
		self.temp += f"{temp}\n"

	def open_in_browser(self,name):
		path = self.create_page(name)

		webbrowser.open(str(path))

"""
	Principe de pogrammation:

		D'abord, on à la possiblité de définir les objets
		css dans un autre module, les importer directements
		dans la définition des balises htmls
"""