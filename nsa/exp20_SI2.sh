#!/bin/bash

echo "Print 3 columns in home directory"

ls -l | cut -c 17-24,39-50,56-

# Printing Column list of files in your home directory. 