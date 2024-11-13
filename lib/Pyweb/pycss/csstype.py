#Coding:utf-8
from .csscore import Css
class setHoverStyle(Css):
	def __init__(self):
		Css.__init__(self)

	def Run_css(self,select):
		select = f'{select}:hover'
		return self.Run_css_(select)

class setActiveStyle(Css):
	def __init__(self):
		Css.__init__(self)

	def Run_css(self,select):
		select = f'{select}:active'
		return self.Run_css_(select)

class setFocusStyle(Css):
	def __init__(self):
		Css.__init__(self)

	def Run_css(self,select):
		select = f'{select}:focus'
		return self.Run_css_(select)

class setVisitedStyle(Css):
	def __init__(self):
		Css.__init__(self)

	def Run_css(self,select):
		select = f'{select}:visited'
		return self.Run_css_(select)

class setUniversalStyle(Css):
	def __init__(self):
		Css.__init__(self)

	def Run_css(self,select):
		select = '*'
		return self.Run_css_(select)

class setChildStyle(Css):
	def __init__(self,selectfille):
		Css.__init__(self)
		self.s_fille = selectfille

	def Run_css(self,select):
		select = f"{select} {self.s_fille}"
		return self.Run_css_(select)

class setNextStyle(Css):
	def __init__(self,nextselect):
		Css.__init__(self)
		self.s_next = nextselect

	def Run_css(self,select):
		select = f"{select} + {self.s_next}"
		return self.Run_css_(select)

class setAttributStyle(Css):
	def __init__(self):
		Css.__init__(self)

	def Run_css(self,select,attr,attrvalue=str()):
		select = f"{select}[{attr}]"
		if attrvalue:
			select = select[:-1]
			select+=f'="{attrvalue}"'
			select+=']'
		return self.Run_css_(select)
