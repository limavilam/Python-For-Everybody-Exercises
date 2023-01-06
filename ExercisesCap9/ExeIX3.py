#Podemos usar el operador lógico no con la condición IF de Python. (IF NOT)
# Las declaraciones dentro del bloque if se ejecutan solo si el valor (booleano) es Falso o si el valor (colección) 
# no está vacío.
rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap7/mbox-short.txt')
#Acá debe ir la ubicación
print (rt)
email_count = dict ()
for line in rt:
    emails =line.split()
    if not line.startswith('From: '): 
        continue
    else:
        if emails [1] not in email_count:
            email_count[emails[1]] = 1
        else: 
            email_count[emails[1]] += 1
print (email_count)


   
