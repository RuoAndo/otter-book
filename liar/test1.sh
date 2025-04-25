r=`shuf -n 1 tmp`
cat zenhan > tmp2
echo "" >> tmp2
echo $r >> tmp2  
cat kouhan >> tmp2

/root/otter-3.3f/bin/otter < tmp2

