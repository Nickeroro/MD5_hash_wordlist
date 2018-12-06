#!/bin/bash

echo  "MD5_wordlist will try to find the salted MD5 hashed messages you've given <3"
echo  "MD5 hashed message should be as it follows: /1 /SALT /THE_SALTED_MD5"
echo  "Input the salt:"
read SALT
echo "Input the MD5 hashed message:"
read H_MD5

while IFS='' read -r line || [[ -n "$line" ]]; do
    	echo "Text read from file: $line"
	OUTPUT="$(openssl $line -1 -salt $SALT)"
	echo "${OUTPUT}"
	
	'if [$OUTPUT = $H_MD5]; then
		echo "$line"
	fi'
	
done < "$1"
