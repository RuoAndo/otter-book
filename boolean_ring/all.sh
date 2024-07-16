#!/bin/sh

TIME1=$(cat /proc/uptime | awk '{print $1}')
echo time1: $TIME1

####

count=0

rm -rf ttt
touch ttt

rm -rf log-all

while read line; do

    echo $line
    ./gen.sh $line &
    
    count=`expr $count + 1`
done < $1

#####

TIME2=$(cat /proc/uptime | awk '{print $1}')
echo time2: $TIME2

DIFF=$(echo "$TIME2 - $TIME1" | bc)
echo diff: $DIFF

echo "count:".$count
