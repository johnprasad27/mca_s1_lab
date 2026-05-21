#!/bin/bash

read -p "Enter directory name you want to search: " dir

for filename in "$dir"/*
do
    if [ -d "$filename" ]
    then
        echo "$filename is a directory"
    else
        echo "$filename is not a directory"
    fi
done