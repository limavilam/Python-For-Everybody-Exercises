xh = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap8/romeo.txt')
print (xh)
lst = list()  #Tengo que crear una lista vacia para que pueda depositar allí la unión de cada una de la palabras. Sin esto no me funcionaria. 
for line in xh:
    line_w = line.rstrip()
    palabras = line_w.split()
    for element in palabras:               
        if element in lst:         
            continue               
        else :                    
            lst.append(element)
lst.sort()
print(lst)
   


