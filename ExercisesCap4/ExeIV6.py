def computepay (h,r):
    if fh > 40: 
        reg = fr*fh 
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
    else: 
        xp = fh * fr 
    return xp

sh = input ('Enter hours:')
sr = input ('Enter rate:')
fh = float (sh)
fr = float (sr)

xp = computepay (fh,fr)
print ('Pay:', xp)
 