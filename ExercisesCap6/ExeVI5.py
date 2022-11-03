str = 'X-DSPAM-confidence: 0.8475'

pos = str.find (':')
number = (str [pos+1:]) #Puedo colocar el 2 porque no contaria el espacio que hay entre los dos puntos y el cero.
print (number)
result = float (number)
print (result)

#Una manera de probar mi código
exmpl = result + 1
print (exmpl)

#Existe otra manera de hacerlo y es seleccionando str por str. 
print (pos)
part = str [pos:]
print (part)
fpart = str [pos+2:]  #Es dos porque hay un espacio
print (fpart)
value = float (fpart)

