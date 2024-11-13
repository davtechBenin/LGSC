#Coding:utf-8

def transform(x):
	if x <= 1:
		x*=100
	return (f"{x}%")

class Css:
	def __init__(self):
		self.cont = str()
		self.Css_dict = dict()
		self.style = str()

	def Set_style(self,objstr):
		self.style+=f"{objstr}\n"

	def Add_css(self,propriete,valeur):
		self.Css_dict[propriete] = valeur

	def Set_mult_css(self,dic):
		for pro in dic:
			self.Add_css(pro,dic[pro])

	def Init_css(self):
		self.cont = str()
		self.Css_dict = dict()

	def Set_min_width(self,value):
		self.Add_css('min-width',value)

	def Set_min_height(self,value):
		self.Add_css('min-height',value)

	def Set_max_width(self,value):
		self.Add_css('max-width',value)

	def Set_max_height(self,value):
		self.Add_css('max-height',value)

	def Set_width(self,value):
		if type(value) in (int,float):
			value = transform(value)
		self.Add_css('width',value)

	def Set_height(self,value):
		if type(value) in (int,float):
			value = transform(value)
		self.Add_css('height',value)

	def Set_size(self,width,height):
		self.Set_width(width)
		self.Set_height(height)

	def Set_overflow(self,value = 'scroll'):
		"""
			Cette méthode est utiliser lorsque l'on veut adapter
			le contenue d'une boite a la taille de la boite. 
			Normalement, cette méthode est utiliser seulement si 
			la largeur et la hauteur de la balise sont définies
			le valeur possible de value sont:
				-> scroll pour cacher le contenue restant mais afficher
					une barre de défillement
				-> visible pour rendre tout simplement visible tout 
					le contenue
				-> hidden permet de cacher le contenue débordente
				-> auto pour laisser le navigateur choisir quoi faire.
		"""
		self.Add_css('overflow',value)

	def Set_display(self,value):
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

			value_dic est un dictionnaire d'attribut.
			il comprend les valeurs
			de positionnement des éléments telque:
				left
				top
				bottom
				right
		"""
		self.Add_css('position',p_type)
		for pro in value_dic:
			self.Add_css(pro,value_dic[pro])

	def Set_position_type(self,typ = 'absolute'):
		self.Add_css('position',typ)

	def Set_margin(self,valeur):
		self.Add_css('margin',valeur)

	def Set_padding(self,valeur):
		self.Add_css('padding',valeur)

	def Set_font_size(self,valeur,Type = "em"):
		# Type peut être 'em' 'px' '%'
		valeur = f'{valeur}{Type}'
		self.Add_css('font-size',valeur)

	def Set_font_family(self,*nom_police):
		"""
			avec la possibilité de mettre plusieurs nom de police à la
			foi, on utilise une liste d'argument non définie.
		"""
		nm = str()
		for i in nom_police:
			nm += f'{i}, '
		nm = nm[:-2]
		self.Add_css('font_family',nm)

	def Set_font_style(self,valeur):
		# valeur doit être soit normal ou italic
		self.Add_css('font-style',valeur)

	def Set_font_weight(self,valeur):
		# la valeur varie de 100 à 900
		self.Add_css('font-weight',valeur)

	def Set_text_decoration(self,valeur):
		# la valeur doit être entre 'underline', 'line-through','none'
		self.Add_css('text-decoration',valeur)

	def Set_underline(self,val = True):
		if val == True:
			self.Add_css('text-decoration','underline')
		else:
			self.Add_css('text-decoration','none')

	def Set_text_align(self,valeur):
		# valeur doit être entre 'left', 'center','right','justify'
		self.Add_css('text-align',valeur)

	def Set_text_color(self,valeur,Type = 'rgb'):
		#type peut être 'rgb', 'rgba', '#' ou str()
		if Type == '#':
			valeur = f"#{valeur}"
		elif Type:
			valeur = f'{Type}{valeur}'
		else:
			valeur = valeur
		self.Add_css('color',valeur)

	def Set_bg_color(self,valeur,Type = 'rgb'):
		#type peut être 'rgb', 'rgba', '#' ou str()
		if Type == '#':
			valeur = f"#{valeur}"
		elif Type:
			valeur = f'{Type}{valeur}'
		else:
			valeur = valeur
		self.Add_css('background-color',valeur)

	def Set_bg_image(self,link,bg_option = dict()):
		"""
		https://developer.mozilla.org/fr/docs/Web/CSS/background pour en savoir plus
			bg_option est un dictionnaire avec les clés suivants:
				attachment valeur(fixed,scroll,local)
				size valeur(cover)
				position valeur(top,bottom,left,center,right)
				origin valeur(border-box,padding-box,content-box)
				repeat valeur(no-repeat,repeat-x,repeat,space,round)
				clip valeur(border-box,padding-box,content-box,text)
		"""
		opt_di = {
			'attachment':'background-attachment',
			'size':'background-size',
			'position':'background-position',
			'origin':'background-origin',
			'repeat':'background-repeat',
			'clip':'background-clip'
		}
		link = f'url({link})'
		self.Add_css('background-image',link)
		for op in bg_option:
			self.Add_css(opt_di[op],bg_option[op])

	def Set_bg_gradient(self,color_stops,direction,color_Type = 'rgb'):
		"""
			color_stops doit être une liste de code. au minimum 2.
			baleur possible de direction:
				180deg -> pour converger vers le bas
				0deg -> pour converger vers le haut
				90deg -> pour converger vers la droite
		"""
		colors = str()
		for color in color_stops:
			if color_Type =='#':
				color = f"#{color}"
			elif color_Type:
				color = f"{color_Type}{color}"
			else:
				color = color
			colors+=f'{color}, '
		colors = colors[:-2]
		value = f"linear-gradient({direction},{colors})"
		self.Add_css('background-image',valeur)

	def Set_opacity(self,valeur):
		# valeur est comprise entre 0 et 1
		self.Add_css('opacity',valeur)

	def Set_border(self,option_dict = dict()):
		"""
			Les valeur possible du dictionnaire sont les suivants:
				width
				color
				style
				position (top,bottom,left,right)
		"""
		dic = {
			"width":"border-width",
			"color":"border-color",
			"style":"border-style",
			"radius":"border-radius",
		}
		if 'position' in option_dict:
			pos = option_dict['position']
			pos = pos.split(' ')
			va = str()
			for i in pos:
				va+=f"{i}-"

			va = va[:-2]
			pos_value = f"border-{va}"
			self.Add_css(pos_value,option_dict['position'])
		for op in option_dict:
			self.Add_css(dic[op],option_dict[op])

	def Set_shadow(self,Hd,Vd,sh,color,colortype='rgb',shadowtype = 'box'):
		pr = f'{shadowtype}-shadow'
		if colortype =='#':
			color = f'#{color}'
		elif colortype:
			color = f'{colortype}{color}'
		valeur = f"{Hd} {Vd} {sh} {color}"
		self.Add_css(pr,valeur)

	def Run_css(self,select):
		self.cont = self.Run_css_only()
		cont = f"""{select}"""
		cont+="{"
		cont+=f'{self.cont}'
		cont+='\n}'
		return cont

	def Run(self):
		return self.Run_css_only()

	def Run_css_(self,select):
		return self.Run_css(select)

	def Run_css_only(self):
		for p in self.Css_dict:
			self.cont+=f'{p}: {self.Css_dict[p]};\n'
		self.cont+=self.style
		return self.cont

	def Set_grid_column(self,start,end):
		self.Add_css('grid-column',f"{start} / {end}")

	def Set_grid_row(self,start,end):
		self.Add_css('grid-row',f"{start} / {end}")


