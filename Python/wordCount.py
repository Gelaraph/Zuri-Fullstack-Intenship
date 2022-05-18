# TASK: Write a python program that counts and returns the number of words in a given text.

# I used str.split() with a string as str to return a list with each 
# element as a word in the string and then used len(iterable) with the list 
# as iterable to count the number of elements.



text = "I am happy to be enrolled in the Zuri intenship";
wordCount = text.split();       #Split the text by white spaces.

numOfWords = len(wordCount);
print(numOfWords);