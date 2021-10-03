

"""
https://stackoverflow.com/questions/11170827/how-do-i-tell-a-python-script-to-use-a-particular-version
https://en.wikipedia.org/wiki/Shebang_(Unix)
"""

"https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size"

from dcode_exercise_1a import my_function, liste_verschieben
'''
https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3#using-from--import
'''

print('Gib die Laenge N der Liste an:')
var1 = input()
num1 = int(var1) # die Zahl N wird abgespeichert in der Variablen num1
print ('Gib die Verschiebung k der Elemente nach rechts an:')
var2 = input()
num2 = int(var2) # die Zahl K wird abgespeichert in der Variablen num2

b = my_function(num1)# hier werden die Werte der 'fertigen' Liste aus dem Modul in der Variablen b abgespeichert
print (my_function(num1)) # hier wird die im Modul definierte Liste auf den Bildschirm ausgegeben,
neueListe2= [] #gebe den Datentyp Liste vor, die keine Werte enthaelt
for everyElement in range(len(b)): # range - Aufruf erzeugt eine Wertetabelle von 0 beginnend bis len(b)-1
    print(len(b))
    IndexElement = [b[everyElement]] #die Innere Klammer gibt den Wert der Liste b mit einem bestimmten Index zurueck. Danach wird der Datentyp 'list' erzwungen
    neueListe2.extend(IndexElement)
    print("Jeder Schritt der for Schleife:", neueListe2)
print("Furz", neueListe2)

print(liste_verschieben(b,num2))



'''
Index from rear:    -6  -5  -4  -3  -2  -1      a=[0,1,2,3,4,5]    a[1:]==[1,2,3,4,5]
Index from front:    0   1   2   3   4   5      len(a)==6          a[:5]==[0,1,2,3,4]
                   +---+---+---+---+---+---+    a[0]==0            a[:-2]==[0,1,2,3]
                   | a | b | c | d | e | f |    a[5]==5            a[1:2]==[1]
                   +---+---+---+---+---+---+    a[-1]==5           a[1:-1]==[1,2,3,4]
Slice from front:  :   1   2   3   4   5   :    a[-2]==4
Slice from rear:   :  -5  -4  -3  -2  -1   :
                                                b=a[:]
                                                b==[0,1,2,3,4,5] (shallow copy of a)


https://stackoverflow.com/questions/509211/understanding-slice-notation/509295#509295
https://stackoverflow.com/questions/14895599/insert-an-element-at-a-specific-index-in-a-list-and-return-the-updated-list

'''

# was passiert bei solchen Aufrufen? https://www.w3schools.com/python/python_functions.asp







"""
itachiobito@DELP1QQCWZ1 MINGW64 ~/Documents/GitHub/git_test (master)
$ py -2 dcode_exercise_1.py
Traceback (most recent call last):
  File "dcode_exercise_1.py", line 16, in <module>
    print my_function()
TypeError: my_function() takes exactly 2 arguments (0 given)

"""

"""
$ py -2 dcode_exercise_1.py
5
Wie lautet N?Traceback (most recent call last):
  File "dcode_exercise_1.py", line 19, in <module>
    print my_function(raw_input('Wie lautet N?'))
  File "dcode_exercise_1.py", line 14, in my_function
    for i in range(1,N): # die For Schleife soll die Liste aufbauen
TypeError: range() integer end argument expected, got str.

"""
