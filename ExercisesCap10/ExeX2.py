rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap7/mbox-short.txt')
#Acá debe ir la ubicación
print (rt)
d = dict ()
lst = list ()
for linea in rt: 
    words = linea.split()
    if len(words) < 3 or words[0]!= 'From': continue 
    else:
        number= words[5].find (':')
        number_hours= words[5] [:number]
        if number_hours not in d:
            d[number_hours] = 1 
        else:
            d[number_hours] +=1 

for key, val in list (d.items()):
    lst.append ((key,val))
    
lst.sort() #No olvidar los paréntesis porque son métodos de un objeto, todos los métodos se llaman con paréntesis. 
#lst.sort(reverse=True) la r es en minúscula y sale en orden de mayor a menor

for key, val in lst:
    print (key,val)


