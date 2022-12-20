rtxt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap7/mbox-short.txt')
print (rtxt)

for line in rtxt: 
    print (line)
    line_w = line.rstrip ()
    print (line_w.upper())