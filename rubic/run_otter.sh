#!/bin/bash

counter=1

while true; do
    echo "[$counter 回目の実行]"

	python3 genrand2.py > tmp
	cat head.txt tmp tail.txt > ${counter}.in

    # 30秒以内に ./otter が終了しなければ強制終了（終了コード 124）
    timeout 10 ./otter < ${counter}.in

    if [ $? -eq 124 ]; then
        echo "10秒経過したため強制終了しました。"
    else
        echo "正常に終了したため、ループを抜けます。"
        break
    fi

    echo "-----------------------------"
    counter=$((counter + 1))
    sleep 4
done
