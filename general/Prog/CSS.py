#Coding:utf-8
"""
	Module de dafinition du format CSS des parties
	de l'accueil.
"""
from lib.Pyweb.balises import Css
from color import *

Main_Css = Css()
Main_Css.Set_bg_color(tuple(MAIN_COL))
Main_Css.Set_position("fixed",{'left':"0%",'top':"0%"})
Main_Css.Set_size(1,1)


Present_Css = Css()
Present_Css.Set_bg_color(tuple(OPTION_COL))
Present_Css.Set_position("fixed",{'left':"2.5%",'top':"5%"})
Present_Css.Set_size(.7,.6)
Present_Css.Set_shadow(5,5,5,(TEXT_COL1))


Connexion_Css = Css()
Connexion_Css.Set_bg_color(tuple(AFF_COL))
Connexion_Css.Set_position('fixed',{'left':'75%','top':"7.5%"})
Connexion_Css.Set_size(.225,.55)


Services_Css = Css()
Services_Css.Set_bg_color(tuple(AFF_COL))
Services_Css.Set_size(.7,.25)
Services_Css.Set_position('fixed',{"left":'2.5%','top':'70%'})
Services_Css.Set_overflow()

Services_T_Css = Css()
Services_T_Css.Set_bg_color(tuple(MAIN_COL))
Services_T_Css.Set_size(.225,.275)
Services_T_Css.Set_position('fixed',{"left":'75%','top':'67.5%'})

