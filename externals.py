"""
External Methods and Classes
Author: Jelle Langedijk
"""
#========================================================
def Load_Data(RelDatLoc:str):
	"""
	Method that loads raw collection data
	"""
	from pandas import DataFrame, read_excel
	from os import system, listdir
	system("pip3 install odfpy")
	dir_items:list = listdir("./")
	if (RelDatLoc in dir_items):
		DF:Dataframe = read_excel(RelDatLoc)
		return DF
	else:
		raise ValueError("Data Location not found!")
#========================================================
def Plotter(DataFrame,cat:str,typ:str="Count",selection:dict=None):
	import plotly.express as px
	import pandas as pd
	if (selection != None):
		for key in selection.keys():
			val = selection[key]
			DF_tmp = DataFrame[DataFrame[key] == val]
	else:
		val		= "All"
		DF_tmp 	= DataFrame
	DF_tmp = pd.DataFrame(DF_tmp[cat].value_counts().rename(typ)).reset_index(level=0).rename(columns = {"index":cat})
	match typ:
		case "Count":
			fig = px.bar(
				DF_tmp,
				x=cat,
				y=typ,
				title=f"{cat} {typ}",
				template="plotly_dark"
				)
			fig.show()
		case "Distribution":
			fig = px.pie(
				DF_tmp,
            	names=cat,
            	values=typ,
            	title=f"{cat} Distribution ({val})",
            template="plotly_dark"
				)
			fig.show()
		case default:
			pass
#========================================================
class GUI(object):
	"""
	Graphical User Interface
	"""
	from ipywidgets import widgets
	import pandas as pd
	def __init__(self,DataFrame:pd.DataFrame):
		self.DF 	= DataFrame

	def DropDownMenu(self,cat):
		dropdown = widgets.Dropdown(
        	options=list(self.DF[cat].unique()),
        	description=f"{cat}: ")
		display(dropdown)
	pass

#========================================================
