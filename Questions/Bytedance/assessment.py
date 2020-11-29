#!/bin/python3

#
# Complete the 'searchSnippet' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING content
#  2. STRING queryW1
#  3. STRING queryW2

import re
import string

def searchSnippet(content, queryW1, queryW2):
    # Write your code here
    
    #Declare vars
    gap = []
    wordFound = [0,0]
    indexes = [-1, -1]
    words = content.split(" ")
    
    #Iterate through the content t find the words
    for index,word in enumerate(words):
        
        #Strip punctuations
        word = word.strip(string.punctuation).lower()
        
        #Set the value to 1
        if word == queryW1.lower():
            wordFound[0] = 1
            indexes[0] = index
        elif word == queryW2.lower():
            wordFound[1] = 1
            indexes[1] = index
        
        if sum(wordFound) < 2:
            continue
        
        #Store gap diff and index
        gap.append(tuple(indexes))
        indexes = [-1,-1]
        wordFound = [0,0]
        
        if word == queryW1.lower():
            wordFound[0] = 1
            indexes[0] = index
        elif word == queryW2.lower():
            wordFound[1] = 1
            indexes[1] = index
        
    #Get the one with the min distance that is the closest
    first,second = min(gap, key = lambda x: max(x) - min(x))
    f = max(0,min(first,second)-3)
    s = min(len(words), max(first,second)+4)
    return " ".join(words[f:s])
        
        