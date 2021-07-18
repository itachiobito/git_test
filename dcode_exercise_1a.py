def my_function(N): # definiere hier eine Funktion, die einen Parameter N braucht
    leere_Liste = [] # ich reserviere Speicherplatz
    for i in range(1,N): # die For Schleife soll die Liste aufbauen
        leere_Liste.append(i) # die Methode append ist eine build in Function bei 'Listen' in python
    return leere_Liste # die Liste wurde um die range erweitert und wird 'zurueckgegeben'; sie ist nicht mehr die leere_Liste, die sie anfangs war
'''
c = my_function(T) ; der Aufruf der Funktion im Modul ist nicht moeglich , da T nicht definiert wurde
print c

itachiobito@DESKTOP-DVP2EOH MINGW64 ~/Documents/GitHub/git_test (master)
$ py -2 dcode_exercise_1.py
Traceback (most recent call last):
  File "dcode_exercise_1.py", line 10, in <module>
    from dcode_exercise_1a import my_function
  File "C:\Users\itachiobito\Documents\GitHub\git_test\dcode_exercise_1a.py", line 7, in <module>
    c = my_function(T)
NameError: name 'T' is not defined


Im Gegensatz dazu wird in der anderen Datei 'dcode_exercise_1' der Paramter N beim Aufruf von 'print my_function(num)' ueber
die Tastatureingabe des Benutzers angegeben und ist damit dem Programm bekannt


'''
