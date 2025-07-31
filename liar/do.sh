#!/bin/bash

# liar: no lex


count=1
rm result
touch result

while read line; do
    echo "[$count] $line"

    cat zenhan > tmp2
    echo "" >> tmp2
    echo "$line" >> tmp2
    echo $line > sos.${count} 
    cat kouhan >> tmp2

    /root/otter-3.3f/bin/otter < tmp2 | tee log.${count}

    grep "clauses generated" log.${count} >> result

    count=$((count + 1))
done < list-sos-3

# python generator.py > list-sos-3
# [root@ik1-314-17351 liar]# tail -f list-sos-3 
# P(says(A,I(C))). P(says(B,I(D))). P(says(C,I(B))). P(says(D,G(C))).
# P(says(A,I(B))). P(says(B,I(C))). P(says(C,I(A))). P(says(D,G(A))).

cat result | sed -E 's/(clauses generated)[[:space:]]+([0-9]+)/\1, \2/' 