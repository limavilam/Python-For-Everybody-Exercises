max = None
min = None 
tot = 0 
keyloop = True 
while keyloop: 
    sval = input ('Enter a number: ')
    try: 
        fval = float (sval)
        tot = tot + 1
        if min is None or fval < min:
            min = fval
        if max is None or fval > max:
            max = fval
    except: 
        if sval == 'Done' or sval == 'done':
            break
        else:
            print ('Invalid Input')
            continue
print (tot, min, max)


