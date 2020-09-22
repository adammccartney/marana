#!/bin/bash
#
# Script to generate all the empty segments for the score
#

declare -i REHEARSAL_MARK=1
for SEGMENT_NAME in A B C D E F G H I K L

do
    cd "segment_$SEGMENT_NAME"
    echo $(python ../genDef.py "$SEGMENT_NAME" "$REHEARSAL_MARK" &)
    cd ..
    REHEARSAL_MARK=$((REHEARSAL_MARK + 1))
done

exit 0
    
