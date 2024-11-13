#Coding:utf-8
from pycss.csssheet import cssSheet
'''
	Cet module permet la 
'''

class htmlSheet(balise):
	def __init__(self,lang = 'fr'):
		balise.__init__(self,'html')
		struc = """<!DOCTYPE html>"""
		self.Set_attr('lang',lang)

	def Set_head(self,head):
		self.Set_cont_obj(head)

	def Set_body(self,body):
		self.Set_cont_obj(body)

	def Get_head(self):
		for obj in self.el_list:
			if obj.bal == 'head': return obj

	def Create_css_file(self,file_name):
		head = self.Get_head()
		head.Set_css_file(file_name)
		
		return cssSheet.Create_css_file(file_name,self.All_css)

	def Append_css_file(self,file_name):
		return cssSheet.Append_css_file(file_name,self.All_css)

	def Read_css_file(self,file_name):
		return cssSheet.Read_css_file(file_name)
