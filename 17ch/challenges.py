#First two challenges to be completed in Bash
#Challenge 1

#Write a regular expression that matches
#the word Dutch in The Zen of Python.

grep Dutch zen.txt

#Challenge 2

#Come up with a regular expression that
#matches all the digits in the string
#Arizona 479, 501, 870. California 209,
# 213, 650.
echo Arizona 479, 501, 870. California 209, 213, 650. | grep [[:digits:]]

#Challenge 3

#Create a regular expression that matches
#any word that starts with any character
#and is followed by two o's. Then use 
#Python's re module to match boo and loo
#in the sentence
#The ghost that says boo haunts the loo.

#Part I - in bash
grep .*oo

#Part II - in Python

import re

re.findall("[bl]oo")

