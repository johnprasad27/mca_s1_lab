#!/bin/bash 
echo "List of below priority jobs" 
ps -al | cut -c 16-19,70- 

# (iii) Listing your job with below normal priority. 

# sed -i 's/\r$//' exp20_SI3.sh
# chmod +x exp20_SI3.sh
# ./exp20_SI3.sh