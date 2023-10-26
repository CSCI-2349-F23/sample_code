#!/bin/bash


### You'll need to have OpenFST and OpenGRM installed to run this code!
### The systems administrator should be installing it soon on cslab.


# build symbol table
ngramsymbols <alldickens.txt > alldickens.syms

# convert sentences in the tokenized file into a binary FSA
farcompilestrings -symbols=alldickens.syms -keep_symbols=1 alldickens.txt > alldickens.far

# count all the n-grams
ngramcount -order=5 alldickens.far > alldickens.counts

# create a model from the couts
ngrammake alldickens.counts > alldickens.mod

# generate a sentence from the model ("sample")
ngramrandgen alldickens.mod | farprintstrings | sed 's/<epsilon>//g' | tr -s ' '

# get the likelihood of a particular sentence

# this one is grammatical and well formed, so it will have a low perplexity
echo "<s> I am a poor boy </s>" | farcompilestrings -generate_keys=1 -symbols=alldickens.syms --keep_symbols=1 | ngramperplexity --v=1 alldickens.mod -

# this one is ungrammatical so it will have a higher perplexity
echo "<s> am poor boy a I </s>" | farcompilestrings -generate_keys=1 -symbols=alldickens.syms --keep_symbols=1 | ngramperplexity --v=1 alldickens.mod -

# this one is grammatical, but it's a lyric from a mid-1990s rap song, so it's
# higher than the first one but lower than the second one
echo "<s> It 's not about a salary it 's all about reality </s>" | farcompilestrings -generate_keys=1 -symbols=alldickens.syms --keep_symbols=1 | ngramperplexity --v=1 alldickens.mod -
