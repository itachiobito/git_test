# diese Funktion erstellt die Liste mit der Laenge N
def my_function(N): # definiere hier eine Funktion, die einen Parameter N braucht
    leere_Liste = [] # ich reserviere Speicherplatz
    for i in range(1,N+1): # die For Schleife soll die Liste aufbauen
    # das Ende des Rangeaufrufs wurde um +1 erhöht, da range nur bis n-1 normalerweise arbeitet.
        leere_Liste.append(i) # die Methode append ist eine build in Function bei 'Listen' in python
    return leere_Liste# die Liste wurde um die range erweitert und wird 'zurueckgegeben'; sie ist nicht mehr die leere_Liste, die sie anfangs war
    # wenn statt leere_Liste ein anderes Wort hier steht , dann funktioniert der Aufruf der Funktion nicht mehr
    # hier stelle ich mir die Frage, was nach dem

#Jolines Funktion

def liste_verschieben(liste, verschiebung=0):
    neue_liste = []

    for i in range(-verschiebung, len(liste) - verschiebung):
        neue_liste.append(liste[i])

    return neue_liste
