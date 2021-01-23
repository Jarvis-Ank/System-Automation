#!bin/bash

function runpy()
{
    cd VScode
    python3 run.py
    echo $1;
}
runpy