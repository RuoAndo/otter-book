#!/bin/bash

rm -rf result-do2
touch result-do2

rm -rf result-do2-plot
touch result-do2-plot

rm -rf result-do2-plot3
touch result-do2-plot3

echo "bidirectional,vertical,horizontal" >> result-do2-plot3
echo "vertical,horizontal" >> result-do2-plot

while read line
do
    r=`echo $line  | cut -d ',' -f 2`
    echo $r
    cat puzzle.$r
    python trans_8puzzle_hot_v.py puzzle.$r > v.$r 
    ./otter-hot < v.$r
    tail_v=`tail -n 1 hot_gen.txt`
    
    python trans_8puzzle_hot_h.py puzzle.$r > h.$r 
    ./otter-hot < h.$r
    tail_h=`tail -n 1 hot_gen.txt`

    tmp=`echo $tail_v","$tail_h | tr -d " "`
    echo $tmp,$line
    echo $tmp,$line >> result-do2

    first=`echo $line | cut -d "," -f 1`
    echo $tail_v","$tail_h | tr -d " " >> result-do2-plot
    echo $first","$tail_v","$tail_h | tr -d " " >> result-do2-plot3
    
done < $1 
