#! /bin/bash

conda activate envCM 

echo  "Enter the .in file u want to read"
read file

var=${file:0:-2}xsf
 
python convert_to_xsf.py $file

python distance.py $var

rm *.xsf
