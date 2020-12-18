#!/bin/bash

./imgToSVG.sh $1
./main.py "$1.svg"
