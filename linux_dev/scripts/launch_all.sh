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
# All output and error messages -- except for the
# ones coming from this script file itself --
# will be redirected to a file named "null_log"
# in the directory "gitnore", as against being
# sent to standard output and standard error
# respectively .
#
# Each piped grep command filters out a file or
# set of files as follows:
#		grep -Ev '.git'			-	folder:	".git"
#		grep -Ev '.sh'			-	files: 		(essentially all script files with names ending in ".sh")
#		grep -Ev '.py'			-	files: 		(essentially all script files with names ending in ".py")
# 		grep -Ev 'penned'	-	file:		follow_my_penned_thoughts.md
#		grep -Evi 'read'		-	files:		README.md; read_list.md
#		grep -Ev 'quo'		-	files:		quote.md; quoraquery.md
#		grep -Ev 'song'		-	file:		songs.md

echo "Launching text files in GEdit ..."
cd log_things_I_do/
for file in `git ls-files | grep -Ev '.git' | grep -Ev '.sh' | grep -Ev '.py' | grep -Ev 'penned' | grep -Evi 'read' | grep -Ev 'quo' | grep -Ev 'song' `;		# loop through the files I'm tracking with git
do gedit $file &>> gitnore/null_log &		# open current file with gedit and redirect output to file: "gitnore/null_log"
done;

echo "Done Launching!"
