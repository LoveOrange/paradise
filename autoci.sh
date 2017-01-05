#!/usr/bin/env bash
if [[ ! $1 ]]
then
    echo 'commit is required'
    exit -1
fi

git add .
git commit -m "$1"
git push origin master
