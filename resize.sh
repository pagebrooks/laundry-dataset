#!/bin/bash

# Quick-and-dirty for resizing raw images using ImageMagick
for i in *.jpg; do
	printf "Resize $i\n"
	convert "$i" -resize 30% "$i"
done

	
