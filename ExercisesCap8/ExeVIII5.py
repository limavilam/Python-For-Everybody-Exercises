rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap7/mbox-short.txt')
#Acá debe ir la ubicación
print (rt)
count = 0
for line in rt:
    line =line.rstrip()
    if not line.startswith ('From: '): continue 
    palabra = line.split()
    print (palabra[1])
    count = count + 1
print ('The total lines: ', count) 


