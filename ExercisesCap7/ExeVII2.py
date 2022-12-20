narchive = input ('Ingrese nombre del archivo:')
try:
    n_archive = open (narchive)
except: 
    print ('Archivo no pudo ser abierto:', narchive)
    exit ()
for str in n_archive:
    if str.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = str.find (':')
        number = (str[pos + 1:])
        result = float (number)
        total = total + result 
average = total/count 
print ('Average spam confidence:', average )