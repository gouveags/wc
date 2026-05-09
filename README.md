# Recreating wc tool

This is my personal attempt to recreate unix wc tool. This project is 100% original, all code in here is 100% mine, NOT AI GENERATED!
It's still cool to be competent, even in the age of AI, so here I'm trying very hard to be cool (maybe being a computer nerd is not the best path to coolness, well, at least I can be cool among my kind) 

I took this challenge following Coding Challenges (awesome) website: https://codingchallenges.fyi/challenges/challenge-wc

# About wc

## How it works

```
wc [...OPTIONS] filename
```


It prints the count of one of these for a given file (or set of files):
- new lines
- words
- bytes
- chars
  
It comes with a set of options to fulfill each count option:
- new lines: -l, --lines
- words: -w, --words
- bytes:  -c ,--bytes
- chars: -m, --chars
  
There are some more options not listed here but still very interesting
