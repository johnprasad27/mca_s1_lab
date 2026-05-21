#!/bin/bash
read -p "Enter first file name: " file1
read -p "Enter second file name: " file2
read -p "Enter third file name: " file3
echo "Enter contents of $file1"
cat > $file1
echo "Enter the conetnts of $file2"
cat > $file2
echo "Difference of $file1 and $file2 saved in $file3"
diff -a $file1 $file2 > $file3
cat $file3

# iii) Print all the difference between two file, copy the two files. 
# meaning
# 2c2  line 2 of first file changed to line 2 of second file
# < line

# line from first file

# > line2

# line from second file
# Meaning of 4,5d3
# 4,5d3

# Means:

# lines 4 and 5 from first file are deleted in second file
# < line4
# < line5

# These lines exist only in first file.