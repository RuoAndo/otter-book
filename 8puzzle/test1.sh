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
    fi
