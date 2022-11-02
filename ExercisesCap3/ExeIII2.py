horas = input ('Enter a number:')
tarifa = input ('Enter a number of hours:')
try:
    ival = int(horas)
    eval = int(tarifa)
except:
    ival = -1 
    eval = -1

if ival > 0:
    print ('Nice Work')
if eval > 0:
    print ('Nice Work')
else: 
    print ('Error, por favor introduzca un número')

# otra manera de hacerlo como menciona el instructor

sh = input ('Enter hours:')
sr = input ('Enter rate:')
try:
    fh = float (sh)
    fr = float (sr)
except:
    print ('Error, por favor introduzca un número:')
    quit ()
#si no pongo el quit va a arrojar error porque no he alcanzado a ejecutar. 
print (fh, fr)