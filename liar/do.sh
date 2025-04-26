#!/bin/bash

count=1
touch result

while read line; do
    echo "[$count] $line"

    cat zenhan > tmp2
    echo "" >> tmp2
    echo "$line" >> tmp2
    cat kouhan >> tmp2

    /root/otter-3.3f/bin/otter < tmp2 | tee log.${count}

    grep "clauses generated" log.${count} >> result

    count=$((count + 1))
done < list-sos-3