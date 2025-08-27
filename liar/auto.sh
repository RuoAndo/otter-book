#!/bin/bash

python generator.py > list-sos
shuf -n5 list-sos > list-sos-tmp

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

    # "clauses generated" の行を result に追加
    r=`grep "clauses generated" log.${count}`
    echo $r
    echo $r >> result
    echo $r > r.${count}

    count=$((count + 1))

done < list-sos-tmp

#cat result | sed -E 's/(clauses generated)[[:space:]]+([0-9]+)/\1, \2/' 

count=6

#touch liar-log
#for ((i=1; i<=count-1; i++)); do
#    g1=`grep "hyper" log.${i} | sed -n 's/.*\] \(P([T]([A-Z]))\)\./\1/p' | awk '!seen[$0]++' | paste -sd,`
#    r1=`cat r.${i} | cut -d " " -f3`
#    r2=`cat sos.${i}`
#    echo $r2","$r1","$g1 >> liar-log
#done

outfile="liar-log-$(date +%Y%m%d-%H%M%S)"

: > "$outfile"   # 空ファイルを用意

for ((i=1; i<=count-1; i++)); do
    g1=$(grep "hyper" "log.${i}" \
         | sed -n 's/.*\] \(P(T([A-Z]))\)\./\1/p' \
         | awk '!seen[$0]++' \
         | paste -sd,)
    r1=$(cut -d " " -f3 "r.${i}")
    r2=$(cat "sos.${i}")
    echo "$r2,$r1,$g1" >> "$outfile"
done

echo "出力ファイル: $outfile"
