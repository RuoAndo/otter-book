count=0

rm -rf log.${1}
touch log.${1}

while read line; do

    rm -rf t.${1}.${count}
    touch t.${1}.${count}

    cat zenhan > t.${1}.${count}
    echo $line >> t.${1}.${count}
    cat kouhan >> t.${1}.${count}

    rm -rf result.${1}.${count}

    TIME1=$(cat /proc/uptime | awk '{print $1}')
    #echo time1: $TIME1
    
    timeout 30 ./otter < t.${1}.${count} > result.${1}.${count}
    rr=`grep "mallocs" result.${1}.${count}`    

    if grep -q "mallocs" result.${1}.${count}; then
       cp result.${1}.${count} result.backup.${1}.${count}
    fi
    
    TIME2=$(cat /proc/uptime | awk '{print $1}')
    #echo time2: $TIME2

    DIFF=$(echo "$TIME2 - $TIME1" | bc)
    
    #echo $line":"$rr | tee -a log.${1}.${count}`
    result=`echo $line":"$DIFF":"$rr`

    echo $result
    echo $result >> log-all


    rm -rf result.${1}.${count}
    rm -rf t.${1}.${count}
    
    count=`expr $count + 1`
done < $1

echo "process "${1}" finished."
