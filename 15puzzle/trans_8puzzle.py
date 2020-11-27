import sys
import re
#import goto, label
#from goto import goto, label


argvs = sys.argv
argc = len(argvs)

f = open(argvs[1]) 

print("set(para_into).")
#print("set(para_from).")

#print("clear(print_kept).")
#print("clear(print_given).")

print("list(usable).")
print("EQUAL(l(hole,l(n(x),y)),l(n(x),l(hole,y))).")
print("EQUAL(l(hole,l(x,l(z,l(u,l(n(w),v))))),l(n(w),l(x,l(z,l(u,l(hole,v)))))).")

print("-STATE(l(n(1),l(n(2),l(n(3),l(end,l(n(4),l(n(5),l(n(6),l(end,l(n(7),l(n(8),l(hole,end)))))))))))).")
print("end_of_list.")

print("list(sos).")


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

        if counter > 1 and counter % 3 == 0 and counter != 9:
            constr = constr + "l(end,"
            
        if counter == 9:
            constr = constr + "end,"
    
        
        #label .END    
            
        counter = counter + 1

    #constr = constr.replace("l(n(hole", "l(hole")
    print(constr.rstrip(",") + ")))))))))))).")

    line = f.readline()

print("end_of_list.")

#print("weight_list(pick_given).")
#print("weight(STATE(l(n(1),l(n($(1)),l(n($(1)),l(n($(1)),l(end,l(n($(1)),l(n($(1)),l(n($(1)),l(n($(1)),l(end,l(n($(1)),l(n($(1)),l(n($(1)),l(n($(1)),l(end,l(n($(1)),l(n($(1)),l(n($(1)),l(hole,end)))))))))))))))))))),0).")
#print("weight(STATE(l(n($(1)),l(n($(1)),l(n($(1)),l(n($(1)),l(end,l(n($(1)),l(n($(1)),l(n($(1)),l(n($(1)),l(end,l(n($(1)),l(n($(1)),l(n($(1)),l(n($(1)),l(end,l(n($(1)),l(n($(1)),l(n(15),l(hole,end)))))))))))))))))))),0).")
#print("end_of_list.")
