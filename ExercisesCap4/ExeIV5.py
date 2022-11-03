def computegrade (calificacion):
    if n >=0.9 and n <=1.0: 
        return ('sobresaliente')
    elif n >=0.8 and n <0.9: 
        return ('Notable')
    elif n >=0.7 and n <0.8:
        return ('Bien')
    elif n >=0.6 and n <0.7:
        return ('Suficiente')
    elif n <0.6 and n >=0.0:
        return ('Insuficiente')
    else:
        return ('Error')
x = input ("Ingrese nota:")
try:
        n = float (x)
except: 
        print ('Error')
        quit ()

calificacion = computegrade(n)

print (calificacion)