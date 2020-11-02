def pyyda_syote(kysy, virhe):
	while True:
		try:		
			vastaus = int(input(kysy))
		except ValueError:
			print(virhe)
		else:
			return vastaus
luku = pyyda_syote(
    "Anna kokonaisluku: ",
    "Et antanut kokonaislukua"
)
print("Annoit kokonaisluvun {}! Nohevaa toimintaa!".format(luku))
hemulit = pyyda_syote(
    "Montako hemulia mahtuu muumitaloon? ",
    "Tämä ei ollut kelvollinen hemulien lukumäärä!"
)
print("Muumitaloon mahtuu {} hemulia".format(hemulit))

	
