"""
WRITE DESCRIPTION
"""
#IMPORTS ============================================
from externals import *

#MAIN ===============================================
def main():
	DF = Load_Data("collection.ods")
	#Plotter(DF,"Format","Distribution",{"Artist":"Live"})
	Plotter(DF,"Artist","Count")



if __name__ == "__main__":
	main()
