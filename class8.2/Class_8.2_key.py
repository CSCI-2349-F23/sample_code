
# Now let's start using nltk. The first thin you need to do is install the nltk library. 
# If you're on cslab, you should know the drill by now

# python3 -m pip install --user nltk

# On your own computer you can leave out --user.

# You will additionally need to download some models and data. 
# The easiest way to do it is to launch the Python interactive terminal. 
# Here's how to do that in a terminal cslab:

# python3
# 
This will give you a Python command line, where the prompt is >>>. 
# Now type these two commands, one at a time:

# import nltk
# nltk.download('popular')

# A bunch of stuff will get downloaded. Then you can quit the Python terminal like this:

# quit()



# And now go get greatexpectations.txt

# ```
# curl http://www.gutenberg.org/files/1400/1400-0.txt > greatexpectations.txt
# ```


#################################################

# enter your import nltk command here and hit Run

import nltk
import re



# ## 3. Loading in the text



f = open("greatexpectations.txt", "r", encoding="utf-8")
alltext = re.sub("\n", " ", f.read())
f.close()


# <code>alltext</code> is a single string containing the entire text of the book. You can see that this is true by printing out the whole thing, but that will take up lots of space. Instead just try printing a random slice, like this:


print(alltext[0:25])
print(alltext[-99:])


# 
# Hint: Be very careful about spaces, case, punctuation, etc. Some regular expressions you will find very useful: <code>+ ^ $ \s .\*</code> and <code>.\*?</code> and the backslash.

# In[8]:


alltext = re.sub("^.*?Chapter I.\s\s\s", "", alltext)
print(alltext[0:25])
alltext = re.sub("\s+\*\*\* END OF THE.*$", "", alltext)
print(alltext[-99:])



# call nltk.word_tokenize here and Run

alltokens = nltk.word_tokenize(alltext)


# line of code for token count
token_count = len(alltokens)

# line of code for type count
type_count = len(set(alltokens))

# line(s) of code for type:token ratio
tt_ratio = type_count / token_count

print(token_count, type_count, tt_ratio)



# Your answers to Q1 demonstrate that there must be some words that were used more than once. Suppose you want to know what are the most frequent words. You can do this using the <code>FreqDist()</code> class in nltk. Run the code below to create a frequency distribution for your list of tokens and to print out the 10 most frequent words and their counts.

# In[11]:


fdist = nltk.FreqDist(alltokens)
fdist.most_common(10)



from nltk.corpus import stopwords
stoplist = stopwords.words('english')
print(stoplist)


# enter your code for appending at least three tokens to the stop list here

stoplist.extend([".", ",", "I", "“", "”", "’", "?", "!", ";", "upon", "could", "would"])


# make a new version of alltokens called allcontenttokens that doesn't contain items from the stop list

print(len(alltokens))
allcontenttokens = [x for x in alltokens if x.lower() not in stoplist]
print(len(allcontenttokens))

# create a new FreqDist from this new version of alltokens
fdist = nltk.FreqDist(allcontenttokens)

# print out the top 10 most frequent tokens in this new FreqDist
fdist.most_common(10)


# The command cell below shows how to use nltk's only true lemmatizer, the WordNet Lemmatizer.

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# an example
print(lemmatizer.lemmatize("dogs"))
print(lemmatizer.lemmatize("speaks", "v"))


# create a new list of tokens, alllemmas by lemmatizing allcontenttokens

alllemmas = [lemmatizer.lemmatize(x) for x in allcontenttokens]


# build a new FreqDist and examine the 50 or 100 most frequent words

fdist_lemmas = nltk.FreqDist(alllemmas)
fdist_lemmas.most_common(50)



