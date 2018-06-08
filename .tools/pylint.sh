#!/bin/sh

SCRIPT_DIR=`cd $(dirname $0); pwd`
PROJECT_DIR=`cd $SCRIPT_DIR/..; pwd`
find $PROJECT_DIR -iname "*.py" | xargs pylint 
