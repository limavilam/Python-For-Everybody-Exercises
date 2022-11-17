rtxt = open ('mbox-short.txt')
for line in rtxt:
    #Se coloca este para eliminar los espacios en blanco
    line_w = line.rstrip()
    print (line_w.upper())