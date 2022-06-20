preis = input('Gib den Preis ein: ')
rabatt_in_prozent = input("Rabatt in %: ")
preis = float(preis)
rabatt_in_prozent = float(rabatt_in_prozent)
rabatt_in_euro = preis/100 * rabatt_in_prozent
neuer_preis = preis - rabatt_in_euro
print('Preis mit', rabatt_in_prozent,"% Rabatt ist")
