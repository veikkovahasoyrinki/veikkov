pelto = [
    [" ", "a", " ", " ", "l"],
    [" ", "k", "@", "k", " "],
    ["h", " ", "a", "k", " "]
]
ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}

kirjaimet = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "i", "k", "l", "m"
	"n", "o", "p", "q", "r", "s", "t", "u", "w", "z", "v", "ä", "ö", "x", "l"]

def tutki_ruutu(merkki, y, x):
	try:
		print("ruudusta ({x}, {y}) löytyy {aasi}".format(x=x, y=y, aasi=ELAIMET[merkki]))
	except KeyError:
		pass
def tutki_kentta(kentta):
	for y, sisalto in enumerate(kentta):
		for x, sis in enumerate(sisalto):	
				tutki_ruutu(sis, y, x)
