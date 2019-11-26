#! /bin/bash

errMsg='call as: dir_contents.sh [-i] directory_path'

case $# in
	1 ) showHidden='false'; dir=$1 ;;
	2 ) showHidden='true';  dir=$2 ;;
	* ) echo $errMsg ; exit -1 ;;
esac

if [[ $showHidden == 'true' ]]; then
	dir=$dir+$dir/.*
fi

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
