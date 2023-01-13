##Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author



import re
rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap11/mbox.txt')
#Acá debe ir la ubicación
print (rt)
count = 0
r_e = input ('Ingrese una expresión regular:')
reg_exp = str(r_e) #Las expresiones regulares son de tipo cadena
for line in rt:
    line = line.rstrip ()
    if re.findall (reg_exp,line)!= []:  #Sale el número que piden en el libro. 
        count = count + 1
        print ('mbox.txt tiene', str(count), 'lineas que coinciden con' + reg_exp)

#Otra manera no correcta de hacerlo pero obtenemos información importante. 
#for line in rt:
    #line = line.rstrip ()
    #if re.search ('reg_exp',line)!= []: #Busca todos y sale un número mayor. 
        #count = count + 1
        #print ('mbox.txt tiene', str(count), 'lineas que coinciden con' + reg_exp)
