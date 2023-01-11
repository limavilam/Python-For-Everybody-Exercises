numlist = list ()
while True: 
    inp = input ('Ingrese el número: ')
    if inp =='Done': break
    try:
        fval = float (inp)
    except: 
        print ('Entrada invalida')
        continue
    valor = int(inp)
    numlist.append (valor)
valor_max= max(numlist)  
#Tener cuidado que es el valor máximo o mínimo de la lista. 
valor_min= min(numlist)
print ('valor_max:', valor_max)
print ('valor_min:', valor_min)