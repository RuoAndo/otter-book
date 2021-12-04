#!/bin/bash

ls hot_gen.txt.* > tmp

rm -rf tmp2
touch tmp2

while read line
do
  #echo $line
  r=`echo $line  | cut -d '.' -f 3`
  #echo $r
  touch hot.$r
  #echo $r >> hot.$r
  r2=`echo $line  | cut -d '.' -f 3`
  r3=`cat puzzle.$r2`

  r4=`tail -n 1 $line | tr -d ' '`
  
  echo $r4,$r,$r3
  echo $r4,$r,$r3 >> tmp2
  #echo $r4,$r,$r3 > hot.$r
done < tmp 

sort -n -k1,1 -t "," tmp2
sort -n -k1,1 -t "," tmp2 > result

