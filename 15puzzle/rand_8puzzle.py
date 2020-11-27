import random

my_list = list(range(1,9)) # list of integers from 1 to 99
                              # adjust this boundaries to fit your needs
random.shuffle(my_list)
#print(my_list) # <- List of unique random numbers

tmpstr = ""
for i in my_list:
  tmpstr = tmpstr + str(i) + ","

print(tmpstr+"hole")
