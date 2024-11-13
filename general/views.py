from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .Prog.Main import Ac_Main

class Main:
	def __init__(self):
		
		self.Ac_main = Ac_Main



	def Run(self,request):
		Obj = self.Ac_main(request)
		path = Obj.create_page("index/index")
		return render(request,path)