#!/bin/bash

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
    
done < $1 
