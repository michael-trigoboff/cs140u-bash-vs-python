#! /bin/bash

printf '%d command line args\n\n' $#

for i in $(seq 0 $#); do
	printf "\$$i=${!i}\n"
done
echo

i=1
for arg in $@; do
	printf '$%d=%s\n' $i $arg
	i=$(( i + 1 ))
done
