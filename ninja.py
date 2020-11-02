huone = [['N', ' ', ' ', ' ', ' '],
         ['N', 'N', 'N', 'N', ' '],
         ['N', ' ', 'N', ' ', ' '],
         ['N', 'N', 'N', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]
"""koordinaatit = [
(x, y)
(x+1, y+1)
(x+1, y-1)
(x-1, y-1)
(x-1, y+1)
(x, y-1)
(x, y+1)
(x+1, y)
(x-1, y)
]"""
def laske_ninjat(xkoordi, ykoordi, huone):	
	x1, x2, x3 = xkoordi, xkoordi - 1, xkoordi + 1
	y1, y2, y3 = ykoordi, ykoordi - 1, ykoordi + 1
	
	koordinaatit = [
	(x1, y1), (x3, y3), (x3, y2), (x2, y2), (x2, y3), (x1, y2), (x1, y3), (x3, y1), (x2, y1)]
	ninjatlkm = 0
	ninjat = []
	for rivi, sis in enumerate(huone):
		ykoord = rivi
		for x, sis in enumerate(sis):
			xkoord = x
			sisalto = sis
			if sisalto == "N":
				ninjat.append(tuple(((xkoord, ykoord))))
			else:
				pass
	for i in koordinaatit:
		if i in ninjat:
			ninjatlkm += 1
		else:
			pass
	print(ninjatlkm)
	
laske_ninjat(2, 3, huone)
"""
	print(ninjatlkm)
		
	#for i in NINJAT:
		#print(NINJAT[i])
	#print(ninjat)

		#for y, sisalto in enumerate(kentta):
		#for x, sis in enumerate(sisalto):	
		#		tutki_ruutu(sis, y, x)
"""
