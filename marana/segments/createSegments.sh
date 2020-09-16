#!/bin/bash
#
# Simple script to generate the segments directory tree within an abjad score
# repo. Execute the script from within ~/<score>/<score>/segments

for SEGMENT_NAME in A B C D E F G H I J K L

do
    mkdir "segment_$SEGMENT_NAME"
    cd "segment_$SEGMENT_NAME"
    touch __init__.py
    touch __metadata__.py
    touch __persist__.py
    touch __layout__.py
    touch definition.py
    touch illustration.ly
    touch .optimization
    cd ..
done

exit 0
