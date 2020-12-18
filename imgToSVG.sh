#!/bin/bash

convert $1 "$1.bmp"
potrace "$1.bmp" --svg
rm "$1.bmp"

