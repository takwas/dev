#!/bin/bash

# ==============
# NOTE:
# ==============
# This script will easy launch all text files
# in the directory in which it is run.
#
# Run this script as:
#    $ ./[script_file_name].sh &       # E.g:  ./launch_all.sh &
# so that it runs without taking hold
# of the terminal.
#
# Also, it will ignore all files/folders
# having the string ".git" in them,
# effectively, ignoring Git version control
# files.
#
# All output and error messages except for the
# ones coming from this script file itself
# will be redirected to a file named "null_log"
# in the directory "gitnore".

echo "Launching text files in GEdit ..."

for file in `git ls-files| grep -Ev '.git'`;
do gedit $file &>> gitnore/null_log &
done;

echo "Done Launching!"
