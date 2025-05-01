#!/bin/bash

count=1
rm result
touch result

# 最初のループ - list-sos-3 の各行を処理
while read line; do
    echo "[$count] $line"

    # zenhan と kouhan の内容を tmp2 に結合
    cat zenhan > tmp2
    echo "" >> tmp2
    echo "$line" >> tmp2
    echo "" >> tmp2
    cat kouhan >> tmp2

    # sos.<count> ファイルに行を出力
    echo "$line" > sos.${count}

    # otter を実行してログを生成
    #/root/otter-3.3f/bin/otter < tmp2 | tee log.${count}
    /root/otter-3.3f/bin/otter < tmp2 > log.${count}

    # "clauses generated" の行を result に追加
    r=`grep "clauses generated" log.${count}`
    echo $r
    echo $r >> result
    echo $r > r.${count}

    count=$((count + 1))
done < list-sos-3

# ２つ目のループ - 各 log.${count} ファイルに対して grep を実行
for ((i=1; i<=count-1; i++)); do
    echo "Processing log.${i}..."    
    # log.${i} に対して指定された grep コマンドを実行
    # grep "hyper" log.${i} | grep -E '^[0-9]+ \[.*?\] P\((I|G)\([A-Z]\)\)\.' 

    #cat log.${i}
    #grep "hyper" log.${i} | sed -n 's/.*\] \(P([IGT]([A-Z]))\)\./\1/p' 
    #grep "hyper" log.${i} | sed -n 's/.*\] \(P([T]([A-Z]))\)\./\1/p' 
    #grep "hyper" log.${i} | sed -n 's/.*\] \(P([T]([A-Z]))\)\./\1/p' | sort | uniq 
    g1=`grep "hyper" log.${i} | sed -n 's/.*\] \(P([T]([A-Z]))\)\./\1/p' | awk '!seen[$0]++' | paste -sd,`

    r1=`cat r.${i} | cut -d " " -f3`
    r2=`cat sos.${i}`

    echo $r2","$r1","$g1


done
