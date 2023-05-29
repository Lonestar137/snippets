#!/bin/bash
buildC() {
    echo "Building C. . ."
    gcc main.c -o ./out/main
    ./out/main
}

buildCPP() {
    echo "Building CPP. . ."
    g++ main.cpp -o out/maincpp
    ./out/maincpp
}

while getopts "cp" opt; do
    case $opt in
    c)
        buildC
        ;;
    p)
        buildCPP
        ;;
    *)
        echo "Invalid option: -$OPTARG"
        exit 1
        ;;
    esac
done
