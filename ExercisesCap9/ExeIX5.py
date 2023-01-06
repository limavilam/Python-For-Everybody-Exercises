rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap7/mbox-short.txt')
#Acá debe ir la ubicación
print (rt)
domain_count = dict ()
for line in rt:
    emails =line.split()
    if not line.startswith('From: '): 
        continue
    else: 
        domain= emails[1].find('@')
        address_domain = emails[1] [domain + 1:]
        if address_domain not in domain_count:
            domain_count [address_domain] = 1
        else: 
            domain_count [address_domain] += 1

print(domain_count)

