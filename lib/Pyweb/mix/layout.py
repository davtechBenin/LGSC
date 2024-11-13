from pyhtml.frequentuse import div

class flexBox(div):
	def __init__(self):
		div.__init__(self)
		self.Begin_css()
		self.Add_css('display','flex')

	def Set_dicrection(self,value):
		"""
			les valeurs possibles de value sont:
				row
				column
				row-reverse
				column-reverse
		"""
		self.Add_css('flex-direction',value)

	def Set_auto_back(self,value='wrap'):
		"""
			les valeurs possibles de value sont:
				nowrap
				wrap
				wrap-reverse
		"""
		self.Add_css('flex-wrap':value)

	def Set_align1(self,value = "space-between"):
		"""
			Les valeurs possibles sont les suivant:
				flex-start
				flex-end
				center
				space-between
				space-around

			Cette méthode permet l'utilisation de 'justify-content' qui
			permet d'alligner les élément sur l'axe principale
		"""
		self.Add_css('justify-content',value)

	def Set_align2(self,value = "center"):
		"""
			Les valeurs possibles sont les suivant:
				flex-start
				flex-end
				center
				stretch
				baseline

			Cette méthode permet l'utilisation de 'justify-content' qui
			permet d'alligner les élément sur l'axe secondaire
		"""
		self.Add_css('align-items',value)

	def Set_align3(self,value,center):
		"""
			Cette méthode utilise 'align-content' qui ne fonctionne que si
			nous avons au moins deux lignes dans notre flexbox.
			les valeur possible de value sont les suivants:
				stretch
				flex-start
				flex-end
				center
				space-between
				space-around
		"""
		self.Add_css('align-content',value)

class gridBox(div):
	"""
		L'utilisation de cet objet nécéssite à ce que les différentes
		taille des éléments placer à l'intérieur ne soit pas fixé.

		Pour une gestion intéligente du positionnement des éléments
		il faut utiliser au lieu des pourcentages, l'unité conçu
		pour ce type dde box. il s'agit du 'fr' soit 'fraction units'
	"""
	def __init__(self):
		div.__init__(self)
		self.Begin_css()
		self.Add_css('display','grid')

	def Set_columns_size(self,*value):
		'''
			value est un ensemble de valeur correspondant
			la largeur de chaque élément à placer dans le
			box.
			cette largeur peuvent être en pixel ou en em ou en %
		'''
		v = str()
		for i in value:
			v+=f' {i}'
		self.Add_css('grid-template-columns',v)

	def Set_rows_size(self,*value):
		'''
			value est un ensemble de valeur correspondant
			la hauteur de chaque élément à placer dans le
			box.
			cette hauteur peuvent être en pixel ou en em ou en %
		'''
		v = str()
		for i in value:
			v+=f' {i}'
		self.Add_css('grid-template-rows',v)

	def Set_columns_auto(self,value):
		'''
			value est un ensemble de valeur correspondant
			la largeur de chaque élément à placer dans le
			box.
			cette largeur peuvent être en pixel ou en em ou en %
		'''
		v = str()
		for i in range(0,value):
			v+=f' 1fr'
		self.Add_css('grid-template-columns',v)

	def Set_rows_auto(self,value):
		'''
			value avec cette méthode doit être le nombre d'éléments
			à ajouter.
			cette hauteur peuvent être en pixel ou en em ou en %
		'''
		v = str()
		for i in range(0,value):
			v+=f' 1fr'
		self.Add_css('grid-template-rows',v)

	def Set_space(self,value):
		"""
			Cette méthode permet d'insérer un peut d'espace entre les éléments
			placés
		"""
		self.Add_css('gap',value)

class customBox(div):
	def __init__(self):
		div.__init__(self)
		self.Begin_css()

	def Set_display(value):
		"""
			Les valeurs de display sont entre autre:
				block : permet convertir un élément en type block
				inline: permet de convertir un élément en type inline
				none: permet de cacher un élément
		"""
		self.Add_css('display',value)

	def Set_position(self,p_type,value_dic):
		"""
			p_type représente le type dde positionnement à chosir.
			parmi ces type, nous avons:
				relative
				fixed
				sticky
				absolute
				unset

			value_dic est un dictionnaire d'attribut. il comprend les valeurs
			de positionnement des éléments telque:
				left
				top
				bottom
				right
		"""
		self.Add_css('position',p_type)
		for pro in value_dic:
			self.Add_css(pro,value_dic[pro])