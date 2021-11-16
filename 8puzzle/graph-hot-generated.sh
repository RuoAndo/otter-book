#!/bin/bash

COUNT=0

while [ $COUNT -lt 10 ]; do

    # 何かの処理

    tail -n 1 hot_gen.txt.${COUNT}
    
    COUNT=`expr $COUNT + 1` # COUNT をインクリメント
done
