#!/bin/bash

# testing the algorithms for each input file
python nearest_neighbor.py -time input_10.txt  
python nearest_neighbor.py -time input_100.txt 
python nearest_neighbor.py -time input_10e5.txt
python nearest_neighbor.py -time input_10e6.txt
