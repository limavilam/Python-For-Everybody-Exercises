xh = input ("Enter Hours: ")
xr = input ("Enter Rate: ")
xp = float (xh) * float (xr)
print ("Pay: ", xp)

xh = input ("Enter Hours: ")
xr = input ("Enter Rate: ")
#si lo dejo así, está mal porque el tipo de dato que tengo al inicio es una cadena, entonces debo convertir la cadena a otra que sí reconozca.
xp = xh * xr
print ("Pay: ", xp)