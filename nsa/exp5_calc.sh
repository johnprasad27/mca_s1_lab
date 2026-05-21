#!/bin/bash

read -p "Enter 2 numbers: " a b
read -p "Enter the operator (+,-,/,*): " op

case $op in
    "+")
        ans=$(echo "$a + $b" | bc)
        ;;

    "-")
        ans=$(echo "$a - $b" | bc)
        ;;

    "*")
        ans=$(echo "$a * $b" | bc)
        ;;

    "/")
        ans=$(echo "scale=2; $a / $b" | bc)
        ;;

    *)
        echo "Invalid operator"
        exit 1
        ;;
esac

echo "$a $op $b = $ans"