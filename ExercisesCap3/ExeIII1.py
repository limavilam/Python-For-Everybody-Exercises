horas = int (input('Ingrese el numero de horas'))
tarifa = float (input('Ingrese tarifa de hora'))
salario= float (horas) * float (tarifa)
print ("El salario es", salario)

#Para el calculo de las horas extra
horas = int (input('Ingrese el numero de horas:'))
tarifa = float (input('Ingrese tarifa de hora:'))
if horas <= 40:
 	print( horas  * tarifa)
elif horas > 40:
	print(40* tarifa + (horas-40)*1.5*tarifa)

#Otra manera de hacerlo como lo hizo el instructor, está es una mejor manera porque separa tanto el str como el float.
sh = input ('Enter hours:')
sr = input ('Enter rate:')
fh = float (sh)
fr = float (sr)

if fh > 40: 
	reg = fr*fh 
	otp = (fh - 40.0) * (fr * 0.5)
	xp = reg + otp
else: 
	xp = fh * fr 
print ('Pay:', xp)