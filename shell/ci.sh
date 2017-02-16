#!/usr/bin/env bash
echo hello world

SVN_WORKSPACE=/Users/lin/projects/test/online/jianglin
GIT_WORKSPACE=/Users/lin/projects/test/online/saber

# svn auto ci
cd ${SVN_WORKSPACE}
sh autoci.sh

# git auto ci
cd ${GIT_WORKSPACE}
sh ci.sh
