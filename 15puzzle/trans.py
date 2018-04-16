import sys
import re
#import goto, label
#from goto import goto, label


argvs = sys.argv
argc = len(argvs)

f = open(argvs[1]) 

print "set(para_into)."
print "set(para_from)."

print "list(usable)."
print "EQUAL(l(hole,l(n(x),y)),l(n(x),l(hole,y)))."
print "EQUAL(l(hole,l(x,l(y,l(z,l(u,l(n(w),v)))))),l(n(w),l(x,l(y,l(z,l(u,l(hole,v)))))))."

print "-STATE(l(n(1),l(n(2),l(n(3),l(n(4),l(end,l(n(5),l(n(6),l(n(7),l(n(8),l(end,l(n(9),l(n(10),l(n(11),l(n(12),l(end,l(n(13),l(n(14),l(n(15),l(hole,end))))))))))))))))))))."
print "end_of_list."

print "list(sos)."


constr = "STATE("

line = f.readline()

while line:

    tmp = line.split(",")

    counter = 1
    
    for x in tmp:
        #print "l(n(" + x.strip() + "),"

        flag = 0

        if x.find("hole") > -1:
            constr = constr + "l(hole,"
            flag = 1
            #GOTO .END

        if flag == 0:
            constr = constr + "l(n(" + x.strip() + "),"

        #if counter == 15:
        #    constr = constr + "l(n(" + tmp[15].strip() + "),end"
        #    break

        if counter > 1 and counter % 4 == 0:
            constr = constr + "l(end," 

        #label .END    
            
        counter = counter + 1

    #constr = constr.replace("l(n(hole", "l(hole")
    print constr.rstrip(",") + ")))))))))))))))))))))."

    line = f.readline()

print "end_of_list."
