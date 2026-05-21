#!/bin/bash


read -p "Enter no of terms: " n

a=0
b=1

for i in $(seq 1 $n)
do
    c=$((a + b))
    echo $a
    a=$b
    b=$c
done

# $ sed -i 's/\r$//' exp17_fibo.sh