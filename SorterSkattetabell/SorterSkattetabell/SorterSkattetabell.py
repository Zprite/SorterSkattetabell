import sys 
import os
from pathlib import Path
'''
SÅNN HER FUNGERER SKATTETABELLEN!

Kolonne 1 (A) tabellID- 4 posisjoner
Kolonne 2 (B) 	 1 - posisjon
Trekkperiode:
1: måned
2: 14 dager
3: uke
4: 4 dager
5: 3 dager
6: 2 dager
7: 1 dag

Kolonne 3 (C) 	- 1 posisjon
Tabelltype
0: Lønn
1: Pensjon
	
Kolonne 4 (D) 	Trekkgrunnlag - 5 posisjoner
Kolonne 5 (E) 	Trekk - 5 posisjoner
'''
årstall = "2020"
def lag_lister(path):
	listeFil = open(path,"r")
	listeLines = listeFil.readlines()
	pathName = Path(path).stem
	file = None
	oldId = None
	os.mkdir(pathName)
	for s in listeLines:

		trekkperiode = s[4:5]
		skatteType = s [5:6]
		if (skatteType == "0" and trekkperiode == "1"):
			id = s[:4]

			if(oldId == None or oldId != id):
				if(not file == None):
					file.close()
				# Lager ny .csv fil med respektivt tabbellnavn 
				file = open(pathName + "/" + id + ".csv", "a")
			oldId = id
			trekkgrunnlag = s[6:11]
			trekk = s[10:16]
			file.write(trekkgrunnlag+';'+trekk+'\n')

try:
	#Laster inn fil fra argumenter. Dra og slipp skattetabellen på .py filen for å kjøre
	skattetabellFil = sys.argv[1]
	print("Lager separate skattelister for" + årstall)
	lag_lister(skattetabellFil)
except Exception as e:
	#print(e)
	print("Dra en fil oppå programmet for å sortere skattelisten")
