#Coding:utf-8
from ..pycss.csssheet import cssSheet
from operator import attrgetter
'''
	Redéfinition des méthode pour l'ajout de contenue au niveau 
	d'un objet balise.
'''
class balise(cssSheet):
	def __init__(self,bal):
		cssSheet.__init__(self)
		self.bal = bal
		self.attrs = str()
		self.cont = str()
		self.attrs_dic = dict()
		self.span_names = list()
		self.All_css = str()
		self.el_list = dict()
		self.def_ind = int()
		self.my_ind = int()

		self.css_n = False

	def Set_span_cont(self,cont,css_name,attrs_dic = dict()):
		sp = balise('span')
		sp.Set_cont(cont)
		sp.Set_attrs(attrs_dic)
		self.span_names+=css_name
		self.Set_cont(sp)

	def Set_cont_obj(self,cont_obj,sup_last = False,ind = None):
		if not ind:
			self.def_ind+=1
			ind = self.def_ind
		if type(cont_obj) == str:
			other = self.el_list.get('all',list())
			cont_obj.my_ind = ind
			other.append(cont_obj)
			self.el_list['all'] = other
		else:
			obj_l = self.el_list.get(cont_obj.Get_name(),list())
			cont_obj.my_ind = ind
			if sup_last:
				obj_l = [cont_obj]
			else:
				obj_l.append(cont_obj)
			self.el_list[cont_obj.Get_name()] = obj_l

	def Get_cont_obj(self,name):
		"""
			Pour la définition du nom de l'objet, il est préférable
			d'appeler la méthode d'instance 'Get_name()' de l'objet
			pour avoir son nom pour éviter les erreurs de nom.
		"""
		return self.el_list.get(name)

	def Sup_cont(self):
		self.el_list = dict()
		self.cont = str()

	def Set_attr(self,attr,value):
		At = f'{attr}="{value}"'
		self.attrs_dic[attr] = value
		self.attrs += f' {At}'

	def Set_css_name(self,name):
		self.Set_attr('class',name)
		self.css_n = True

	def Get_css_name(self):
		return f".{self.Get_attr('class')}"

	def Set_attrs(self,attrs_dic):
		for attr_name in attrs_dic:
			self.Set_attr(attr_name,attrs_dic[attr_name])

	def Get_attr(self,attr):
		at = self.attrs_dic.get(attr)
		return at

	def Set_name(self,name):
		self.Set_attr("name",name)

	def Get_name(self):
		if 'name' in self.attrs_dic.keys():
			return f".{self.attrs_dic['name']}"
		elif 'id' in self.attrs_dic.keys():
			return f"#{self.attrs_dic['id']}"
		else:
			return self.bal

	def Set_id(self,Id):
		self.Set_attr("id",Id)

	def Set_style(self,style):
		"""
			style doit être un objet de définition de css
		"""
		if type(style) != str:
			style = style.Run()
		self.Set_attr("style",style)

	def Set_type(self,Type):
		self.Set_attr("type",Type)

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
		el_li = list()
		for el in self.el_list.values():
			if type(el) == list:
				el_li.extend(el)
			else:
				el_li.append(el)
		el_l = sorted(el_li,key = attrgetter('my_ind'))
		for e in el_l:
			self.cont += e.Run_html()

		Ct = f"""\n<{self.bal} {self.attrs}>{self.cont}\n</{self.bal}>"""
		return Ct

	def Get_css(self,**kwarg):
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

		self.All_css = self.Run_css(select,**kwarg)
		
		for el in self.el_list.values():
			if type(el) == list:
				for e in el:
					if e.All_css:
						self.All_css+=el.All_css
					else:
						self.All_css+= el.Get_css()
			else:
				if e.All_css:
					self.All_css+=el.All_css
				else:
					self.All_css+= el.Get_css()

		return self.All_css

class baliseOrph(balise):
	def __init__(self,bal):
		balise.__init__(self,bal)

	def Run_html(self):
		Ct = f"""\n\t<{self.bal} {self.attrs}/>"""
		return Ct

