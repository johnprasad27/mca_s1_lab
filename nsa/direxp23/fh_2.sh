#!/bin/bash
echo "Number of lines: $(wc -l < myfile)"
echo "Number of words: $(wc -w < myfile)"
echo "Number of characters: $(wc -c < myfile)"

# 6. Print the contents of the 3rd row only of the file myfile. 

echo "3rd Row:"
sed -n '3p' myfile


# 7.  Append the contents of myfile into a file called myappendfile without 
# rewriting the contents of myappendfile. 

cat myfile >> myappendfile