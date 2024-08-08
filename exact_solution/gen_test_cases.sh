#!/bin/bash

vertex_count=$1
step_count=$2

if [[ -z $vertex_count ]]; then
    echo "Missing parameter for vertex count, please try running the script again."
    echo "bash run_test_cases.sh [vertex_count] [step_count]"
    exit
elif ! [[ "$vertex_count" =~ ^[0-9]+$ ]]; then
    echo "Vertex count is not a valid number, please try running the script again."
    echo "bash run_test_cases.sh [vertex_count] [step_count]"
    exit
elif [[ -z $step_count ]]; then
    echo "Missing parameter for step count, please try running the script again."
    echo "bash run_test_cases.sh [vertex_count] [step_count]"
    exit
elif ! [[ "$step_count" =~ ^[0-9]+$ ]]; then
    echo "Step count is not a valid number, please try running the script again."
    echo "bash run_test_cases.sh [vertex_count] [step_count]"
    exit
fi

cp /dev/null times.txt

file_count=0

for (( i=5 ; i<=150 ; i=i+$step_count ));
do
    let x=$file_count y=1 file_count=x+y
    if ! python generate_test.py $vertex_count $i $file_count; then
        exit
    fi

    approx_dir="../approx_solution/test_cases"
    file="test_cases/input"$file_count".txt"
    cp $file $approx_dir

    if [ "$i" -ge 100 ]; then
        exit
    fi
done