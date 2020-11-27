import csv
import sys

args = sys.argv
csv_file = open(args[1], "r", encoding="ms932", errors="", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

#print(f)

counter = 0
counter2 = 0

judge = []

holeplace = 0
counter = 1

line = []

for row in f:
    for i in row:
        line.append(i)

#print(line)

counter = 1
for i in line:
    print(str(i) + ":" + str(counter))
    if i == "hole":
        print("hole->" + str(counter))
        #print(int((counter%4)+1))
        if counter > 1 and counter < 4:
            holeplace = 1
        if counter > 4 and counter < 7:
            holeplace = 2
        if counter > 7 and counter < 10:
            holeplace = 3
            
    counter = counter + 1

print("hole at line: "+str(holeplace))
print("###")
    
line.remove("hole")
print(line)

print("###")

counter = 0
for i in line:
    #print(i)                
    nw = line[counter:]
    print(i + "->" + "[" + ','.join(nw) + "]")
        
    counter2 = 0
    for j in nw:
        print("compare:" + str(i) + ":" + str(j))
        if int(i) > int(j):
            counter2 = counter2 + 1
            print("smaller! ->" + str(j))

    print("result:" + str(counter2))
            
    judge.append(counter2)            
    counter = counter + 1

print(judge)

sum = 0
for i in judge:
    sum = sum + i
    
print(sum)
print(holeplace)
