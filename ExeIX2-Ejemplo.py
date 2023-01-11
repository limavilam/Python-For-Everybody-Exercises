rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap7/mbox-short.txt')
#Acá debe ir la ubicación
print (rt)
counts = dict()
for line in rt:
    words =line.split()
    for word in words:
        counts [word] = counts.get(word,0)+1

for line in rt:
    words = line.split()    
    if len(words) < 3 or words[0]== 'From': continue
   
    words = words[2]
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)


