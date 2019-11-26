#! /bin/bash

# check for presence of ONE command line arg
if [[ $# != 1 ]]; then
	echo 'call with directory path'
	exit -1			# return "false"
fi

dir=$1

printf "contents of $dir\n\n"
for item in $dir/*; do
    if [[ -d $item ]]; then
		printf 'dir:  '
	else
		printf 'file: '
	fi;
	printf '%s\n' $(basename $item)
done

exit 0				# return "true"
