#!/bin/bash
read -p "Enter a string : " str
read -p "Enter the starting index and no of caharacters: " a b
substr=${str:$a:$b}
echo "Substring : $substr"