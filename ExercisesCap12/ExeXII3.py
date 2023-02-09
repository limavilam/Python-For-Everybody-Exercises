import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
count = 0
for line in fhand:
    words = line.decode().split()
    count = count + len(words)
    if count < 3000:
        print(line.decode().strip())
print(count)

