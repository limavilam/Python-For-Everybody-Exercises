#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772

import re
rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap11/mbox.txt')
#Acá debe ir la ubicación
print (rt)
lst =list()

for line in rt:
    line = line.rstrip()
    x = re.findall('^New Revision:(\s[0-9.]+)',line)
    if len(x) > 0:
        for number in x:
            number = float(number)
        lst.append(number)
avg = sum(lst)/len(lst)
print(avg)
