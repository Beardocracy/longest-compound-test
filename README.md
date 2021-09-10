# Longest-compound:

### To run program, in a console:
    ./run.sh
    
## Problem:
Write a program that reads a file containing a sorted list of words (one word per line, no spaces, all lower case), then identifies the longest word in the file that can be constructed by concatenating copies of shorter words also found in the file.

### Input:
The program should read the words from https://gist.github.com/bobbae/4ca309a1857158d5766d4ede4235cae0.
> See note 1 for more information

### Output:
* Longest compound word
    * Actual longest word: **`dichlorodiphenyltrichloroethane`**
* Total number of compound words
 

## Algorithm:
### Data Structure:
* Trie (Prefix Tree)
* https://www.youtube.com/watch?v=hjUJFjcrbR4
* See note 2

Once the tree is built, the program goes through the list of words again, using the `is_compound` function.

_Every **compound word** will have a point a prefix ends, and the rest of the string making up the word is also it's own word._

The `is_compound` function walks through a word left to right, walking down the completed trie step for step. When it comes to a node in the trie that has an asterisk (which signifies the ending of a word, or prefix in this case), it checks to see if everything right of the asterisk is also a word. If it is, we return True. If not, we call `is_compound` again for only the remaining piece of the word (after the asterisk).

## Notes:
1. For data input I decided to create a file from the words in the given url and push that to the repo.
 _I built the ability for the program to take the gist url as input, but left it commented out because the I felt the requirements were ambiguous in this regard, and reading from the file makes the program simpler._
 _Additionally, if you attempt to run the program on a computer without the `requests` module, you will get a 'module not found' error._

2. Prior to taking on this project, I didn't know the trie data structure existed. A quick google search yielded the the best data structure for this problem, and I used the first ~13 minutes of this video as a to get me started in creating the initial structure. The video is not specific to this problem, and the solution was created from scratch without further assistance.
    > https://www.youtube.com/watch?v=hjUJFjcrbR4
    > Author: Nathan Patnam
