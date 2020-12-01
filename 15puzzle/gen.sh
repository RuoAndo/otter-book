COUNT=0
while [ $COUNT -lt 10 ]; do

    python rand_8puzzle.py > tmp
    python judge_8puzzle.py tmp > tmp2
    result=`tail -n 1 tmp2`
    echo $result
    
    if [ $((${result} % 2)) = 1 ]; then
	echo "奇数だよ"

    # cl_generated.txt  cl_kept.txt  for_sub.txt  sos_size.txt
	
    else
	echo "偶数だよ"
	brd=`cat tmp`
	echo "BOARD:"${brd}
	python trans_8puzzle.py tmp > tmp3
	otter < tmp3
	
	cp cl_generated.txt cl_generated.txt.${COUNT}
	cp cl_kept.txt cl_kept.txt.${COUNT}
	cp for_sub.txt for_sub.txt.${COUNT}
	cp cl_kept.txt cl_size.txt.${COUNT}
	
	COUNT=`expr $COUNT + 1` # COUNT をインクリメント
    fi

done
