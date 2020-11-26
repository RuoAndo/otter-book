import random

my_list = list(range(2,16)) # list of integers from 1 to 99
                              # adjust this boundaries to fit your needs
random.shuffle(my_list)
#print(my_list) # <- List of unique random numbers

tmpstr = "1,"
for i in my_list:
  tmpstr = tmpstr + str(i) + ","

print(tmpstr+"hole")
