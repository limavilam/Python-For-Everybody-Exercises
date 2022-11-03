num = 0 
tot = 0.0
while True :
    sval = input ('Ingrese el número: ')
    if sval =='Done' :
        break 
    try:
        fval = float (sval)
    except: 
        print ('Entrada invalida')
        continue
    fval = float (sval)
    print (fval)
    num = num + 1
    tot = tot + fval 

print ('Done')
print (tot, num, tot/num)