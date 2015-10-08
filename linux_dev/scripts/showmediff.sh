#!/bin/bash
echo
echo "==========================================="
echo "   Showing files with changes ..." | grep -E 'Showing';
diff ~/log_things_I_do/ . | grep 'diff' | grep -Ev 'showmediff' | grep -E 'diff';
echo "-------------------------------------------"
echo "   Showing files out of sync ..." | grep -E 'Showing'
diff ~/log_things_I_do/ . | grep -E 'Only.*[^~]$' | grep -Ev 'git' | grep -Ev 'working_on' | grep -E 'Only'
echo
echo "==========================================="
