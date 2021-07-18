

"""
https://stackoverflow.com/questions/11170827/how-do-i-tell-a-python-script-to-use-a-particular-version
https://en.wikipedia.org/wiki/Shebang_(Unix)
"""

"https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size"

from dcode_exercise_1a import my_function
# https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
# print('Gib die Laenge N der Liste an:')
var = input()
num = int(var)
b = my_function(num) # hier speichere ich den Rueckgabewert aus der Datei dcode_exercise_1a in einer neuen Variablen ab
print my_function(num)
print b


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
