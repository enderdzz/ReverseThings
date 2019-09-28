#!/bin/sh

for file in ./*
do
    # uncompyle6 -o PYC0.pyc.py PYC0.pyc
    uncompyle6 -o $file.py $file
done
