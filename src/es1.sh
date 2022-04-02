#!bin/bash

func(){
filename=$1
a=$2
b=$3
c=$4
echo “Sono $1 e ho $# argomenti e i primi tre sono:”
echo $a
echo $b
echo $c
if [[($#==“-h”)]] 
then
echo -e "\nUso: $1 parametri \n"
exit 0
fi
}
func mydata 4 24 35 


  
