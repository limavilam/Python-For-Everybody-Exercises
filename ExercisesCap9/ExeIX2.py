rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap7/mbox-short.txt')
#Acá debe ir la ubicación
print (rt)
counts = dict()
for line in rt:
    words = line.split()    
    if len(words) < 3 or words[0]!= 'From': continue  
    #Si lo pongo == me van a salir todas las que son iguales depués del from. No olvidar que != (Not equal)
    #si solo pongo if len(words) < 3 : continue; la salida del programa son la cantidad de letras solas. 
    else:
        if words[2] not in counts:
            counts[words[2]] = 1       
        else:
            counts[words[2]] += 1      
print (counts)
