#!bin/bash
declare -i a=43
declare -i b
read -r b
if [[("$a" -gt "$b")]]
then
echo “a è maggiore di b”
fi
if [[("$a" -lt "$b")]] 
then 
 echo “a è minore di b”
fi
if [[("$a" -eq "$b")]]
then 
echo “a è uguale a b”
fi
