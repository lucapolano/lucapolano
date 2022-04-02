#!bin/bash
loop() {
if [-z $1] 
then 
N=10
fi
N = $(($1))
for ((i=1; i<=N; i+=1));
do 
echo $i
done 
}

read N
loop N
