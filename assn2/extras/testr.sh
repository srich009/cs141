#!/bin/bash

touch out.dat

for i in {1..10}
do
    python3 assignment2.py -both input1.txt >> out.dat
    printf '\n' >> out.dat
done
