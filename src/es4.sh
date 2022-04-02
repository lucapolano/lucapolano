#!bin/bash
read a
case $a in 
	start)
	echo “system started”
;;
	stop)
	echo “system stopped”
;;
	restart)
	echo “system stopped”
	echo “system started”
;;
esac
