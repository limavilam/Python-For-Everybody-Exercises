nota = (input ("Ingrese nota:"))
x = float (nota)
if x < 0.6: 
    print ('Insuficiente')
elif x >= 0.6: 
    print ('Suficiente')
elif x >= 0.7:
    print ('Bien')
elif x >= 0.8:
    print ('Notable')
elif x >= 0.9:
    print ('Sobresaliente')
else:
    print ('Error')

#El orden es importante, el anterior código está bien escrito pero no se ejecuta como quiero, error semántico, este código no va a responder toda mi prgunta.  
x = float (input ("Ingrese nota:"))
if x >= 0.9 and x <= 1.0: 
    print ('sobresaliente')
elif x >= 0.8 and x < 0.9: 
    print ('Notable')
elif x >= 0.7 and x < 0.8:
    print ('Bien')
elif x >= 0.6 and x < 0.7:
    print ('Suficiente')
elif x < 0.6 and x >= 0.0:
    print ('Insuficiente')
else:
    print ('Error')

#Este código sí es el correcto
x = input ("Ingrese nota:")
#No puedo poner x en los If porque x es una variable de tipo str, así que debo usar la variable de tipo float. 
try:
    n = float (x)
except: 
    print ('Error')
    quit ()
if n >=0.9 and n <=1.0: 
    print ('sobresaliente')
elif n >=0.8 and n <0.9: 
    print ('Notable')
elif n >=0.7 and n <0.8:
    print ('Bien')
elif n >=0.6 and n <0.7:
    print ('Suficiente')
elif n <0.6 and n >=0.0:
    print ('Insuficiente')
else:
    print ('Error')
