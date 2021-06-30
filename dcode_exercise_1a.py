def my_function(N): # definiere hier eine Funktion, die einen Parameter N braucht
    leere_Liste = [] # ich reserviere Speicherplatz
    for i in range(1,N): # die For Schleife soll die Liste aufbauen
        leere_Liste.append(i) # die Methode append ist eine build in Function bei 'Listen' in python
        
    return leere_Liste # die Liste wurde um die range erweitert und wird 'zurueckgegeben'; sie ist nicht mehr die leere_Liste, die sie anfangs war
