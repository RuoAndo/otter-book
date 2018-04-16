import sys
import re

argvs = sys.argv
argc = len(argvs)

f = open(argvs[1]) 

print "graph G {"

line = f.readline()

counter = 0
while line:

    tmp = line.split(",")
    
    for x in tmp:
        if x.find("hole") > -1:
            print "0;"
        else:
            print x.strip() + ";"
        
    line = f.readline()

print "}"
