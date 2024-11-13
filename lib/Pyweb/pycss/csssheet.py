#Coding:utf-8
from .csscore import Css
from .csstype import *
from .cssconst import DESKTOP
class cssSheet:
	def __init__(self):
		"""
			les valeurs possible pour la définition d'un style css sont:
				Normal
				Hover
				Active
				Focus
				Visited
				Universal
				Child
				Next
				Attribut

			Le principe ici, est que, nous utilisons un dictionnaire.
			ce dictionnaire permet de stocker toute les propriétés css
			que l'on veut définir. la variable self.css est détruite 
			chaque foi que nous appelons la méthode End-css(). mais
			elle est initialiser a chaque appel de la méthode Begin_css()
		"""
		self.dic = {
		'Normal' : Css,
		'Hover' : setHoverStyle,
		'Active' : setActiveStyle,
		'Focus' : setFocusStyle,
		'Visited' : setVisitedStyle,
		'Universal' : setUniversalStyle,
		'Child' : setChildStyle,
		'Next' : setNextStyle,
		'Attribut' : setAttributStyle,
		}
		self.my_css = dict()

		self.child_ind = int()
		self.next_ind = int()
		self.attribut_ind = int()

	def Begin_css(self,*css_arg,css_type = 'Normal'):
		self.css_t = css_type
		obj = self.dic[css_type](*css_arg)
		if css_type not in ('Child','Next','Attribut'):
			self.css = self.my_css.get(css_type,obj)
		else:
			return obj

	def Begin_css_(self,suiv_name,css_t,suiv_type = 'None'):
		"""
			l'argument suiv_name spécifie le nom de référence
			de la balise à qui le style veut être attribuer
			celui de suiv_type permet de spécifier si le nom
			fait reférence à une classe, un id ou une balise. par
			défaut, la configuration est fait sur une balise. 
			Les valeurs possibles de suiv_type sont:
				-> 'None' par défaut et permet de dire qu'l
					s'agit d'une balise
				-> 'class' pour dire qu'il s'agit d'une classe 
				-> 'id' pour dire qu'l s'agit d'un id
		"""
		if suiv_type == 'None':
			suiv_name = suiv_name
		if suiv_type == 'class':
			suiv_name = '.' + suiv_name
		if suiv_type == 'id':
			suiv_name = '#' + suiv_name
		obj = self.Begin_css(suiv_name,css_type =css_t)
		return obj

	def Begin_child_css(self,child_name,child_type='None',ind = None):
		obj = self.Begin_css_(child_name,'Child',child_type)
		if ind:
			typ = css_t+str(ind)
		else:
			self.child_ind +=1
			typ = css_t+str(self.child_ind)
		self.css_t = typ
		self.css = self.my_css.get(typ,obj)

	def Begin_next_css(self,next_name,next_type='None',ind = None):
		obj = self.Begin_css_(next_name,'Next',next_type)
		if ind:
			typ = css_t+str(ind)
		else:
			self.next_ind +=1
			typ = css_t+str(self.next_ind)
		self.css_t = typ
		self.css = self.my_css.get(typ,obj)

	def End_css(self):
		self.my_css[self.css_t] = self.css
		del self.css
	
	def Run_css(self,select):
		'''
			C'est la méthode utilisée pour céer une suite de chaine 
			composée des propriété css définie.

			Avec cette méthode, on donne une paramètre nommé avec le nom
			du style que nous voulons appliquer. 
		'''
		css_str = str()
		for typ in self.my_css:
			css_str+=self.my_css[typ].Run_css(select)
			css_str+='\n'
		return css_str

	def Run_css_(self,select):
		return self.Run_css(select)

	@classmethod
	def Create_css_file(cls,file_name,css):
		with open(file_name,'w') as fic:
			fic.write(css)
		return len(css)

	@classmethod
	def Append_css_file(cls,file_name,css):
		with open(file_name,'a') as fic:
			fic.write(f"\n{css}")
		return len(css)

	@classmethod
	def Read_css_file(cls,file_name):
		with open(file_name,'r') as fic:
			data = fic.read()
		return data

class generalCss(cssSheet):
	"""
		Cette classe est utilisée pour définire un ensemble 
		de style Css pour la gestion d'un ensemble composé 
		de balise. Cette classe est initialisée avec un 
		élément de base. généralement le body (qui est la
		définition par défaut.). par le suite, nous avons
		la possibilité de définir un ensemble de style pour
		une balise spécifique de la balise principale sans
		problème. 

		L'utilisation de cet objet est indépendant et n'est 
		pas pris en héritage par une classe de simulation
		html par défaut.
	"""
	def __init__(self,bal = 'body'):
		cssSheet.__init__(self)
		"""
			L'utilisation de l'objet lui-même permet de définir
			une suite de style directement lié à la balise de 
			base.
		"""
		self.child_css = dict()
		self.bal = bal

	def Add_child_css(self,bal,bal_typ = 'None'):
		"""
			Cette méthode est utilisée pour définir un style 
			css spécifique à une balise fille de la balise
			de base. elle retourne une objet cssSheet.
			le comportement est le même que l'objet de base
			seulement que, même si cette balise définie une
			balise fille, la définition du style css de 
			cette balise se pasera toujours par une nouvelle 
			appelation de cette méthode.

			La variable d'intance BAL n'est pas propre 
			à l'objet de définition de base.

			les valeurs possible de bal_typ sont:
				-> 'None' --> une balise
				-> 'class' --> une classe
				-> 'id' --> un id
		"""
		if bal_typ == 'None' or bal_typ == None:
			bal = bal
		elif bal_typ == 'class':
			bal = f".{bal}"
		elif bal_typ == 'id':
			bal = f'#{bal}'

		obj = self.child_css.get(bal,cssSheet())
		obj.BAL = bal
		return obj
	
	def Add_childs_css(self,*child):
		chs = str()
		for c in child:
			chs +=f'{c},'
		chs = chs[:-1]
		obj = self.child_css.get(chs,cssSheet())
		obj.BAL = chs
		return obj

	def Update_child_css(self,*cssobj):
		for obj in cssobj:
			self.child_css[obj.BAL] = obj

	def Run_css(self):
		All_css = self.Run_css_(self.bal)
		for nam in self.child_css:
			css = self.child_css[nam]
			All_css += css.Run_css(nam)
		return All_css

	def Def_css_sheet(self,sheet_name):
		"""
			Cette méthode sera légèrement modifier au moment
			de la finalisation de l'outils pour spécifier le
			dossier où insérer les fichiers css.
		"""
		css = self.Run_css()
		if sheet_name[-4:] != '.css':
			sheet_name = f'{sheet_name}.css'
			with open(sheet_name,'w') as fic:
				fic.write(css)
		return len(css)

class cssPage:
	def __init__(self,media_type = 'screen' ,media_value = DESKTOP):
		'''
			les attribut optionnelle permet la création de site
			en prenant en compte le type de périphérique sur lequel
			s'affichera votre site.

			les valeurs possible de media_type:
				-> screen : pour spécifier le style uniquement les 
					écran
				-> all : pour spécifier tout type de média
				-> print: pour formater un contenu pour l'imprimer

			Les valeurs possible de media_value sont à choisir
			au niveau des Constantes pré-définie. mais l'utilisateur
			peut lui même créer ses propres valeurs.
		'''
		self.media_type = media_type
		self.media_value = media_value

		self.All_css = dict()

	def Set_css_obj(self,css_obj,select):
		self.All_css[select] = css_obj

	def Get_css_obj(self,select):
		return self.All_css.get(select,generalCss(bal=select))

	def Run(self):
		self.media = f"@media {self.media_type} and {self.media_value}"
		self.media += '{\n'
		for select in self.All_css:
			obj = self.All_css[select]
			self.media += obj.Run_css()
		self.media += '\n}\n'
		return media

