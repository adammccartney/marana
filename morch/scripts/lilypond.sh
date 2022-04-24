#!/bin/bash

trap 'rm -f "$TMPFILE"' EXIT

TMPFILE=$(mktemp) || exit 1

if [ "`which timeout`" != "" ]; then
        TIMEOUT="timeout 1m"
else
        TIMEOUT=
fi

LANG=C $TIMEOUT lilypond $1 2>$TMPFILE

res=`grep -E "warning: (barcheck failed|strange time signature found)" $TMPFILE`

# test for detected error
test "$res" == ""
