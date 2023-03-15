import re
#In this assignment you will read through and parse a file with text and numbers. 
# #You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1543746.txt (There are 102 values and the sum ends with 42)

import re
rt = open ('c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap11/regex_sum_1543746.txt')
lst =list()

for line in rt:
    x = re.findall('[0-9]+',line)
    lst = lst + x
sum=0
for number_a in lst:
    sum = sum + int(number_a)
print (sum)

import re

hand = open("c:/Users/limav/OneDrive/Documentos/Machine/P4EB/Exer-Python4Everybody/PythonExeBook/ExercisesCap11/regex_sum_42.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
