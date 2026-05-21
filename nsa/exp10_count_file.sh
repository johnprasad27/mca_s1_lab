#!/bin/bash

read -p "Enter directory name you want to search: " dir

direct="/mnt/c/Users/john27/MCA/mca_s1/lab/nsa/$dir"

if [ -d "$direct" ]
then
    num_files=$(find "$direct" -type f | wc -l)
    echo "There are $num_files files in $direct"
else
    echo "$direct is not a directory"
fi