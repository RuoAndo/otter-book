python rand_8puzzle.py > tmp
python judge_8puzzle.py tmp > tmp2
result=`tail -n 1 tmp2`
echo $result

if [ $((${result} % 2)) = 1 ]; then
    echo "奇数だよ"
else
    echo "偶数だよ"
    python trans_8puzzle.py tmp > tmp3
    otter < tmp3
fi    
