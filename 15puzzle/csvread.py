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

for row in f:
    for i in row:
        print(i)
        if i == "hole":
            holeplace = counter %4
            print(":"+str(counter%4))
        counter = counter + 1

print(f)

counter = 0        
for row2 in f:
    print(row2)
    row.remove("hole")
    for i in row:
        print(i)                
        nw = row[counter:]
        print(nw)
        
        counter2 = 0
        for j in nw:
            if i > j:
                counter2 = counter2 + 1

        judge.append(counter2)
                
        counter = counter + 1

print(judge)

sum = 0

for i in judge:
    sum = sum + i

print(sum+holeplace) 
