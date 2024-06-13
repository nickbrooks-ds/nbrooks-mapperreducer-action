#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 

def valid_word(word):
  for character in word:
    if character not (('A' <= character <= 'Z') or ('a' <= character <= 'z') or (character == "'")):
      return False
  return True
  
for line in sys.stdin: 
    line = line.strip() 
    words = line.split() 
    for word in words:
      if valid_word(word):
        print('%s\t%s' % (word, 1))
