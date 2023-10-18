# Class 8.2: NLTK for tokenizing, normalizing, and lemmatizing text

Today we will be learning a bit about how to use the Python library <code>nltk</code> to do tokenization, normalization, lemmatization, and stop word management.

### **A note on Jupyter notebooks**
I'm demonstrating using a Jupyter notebook, but I'll be also sharing the code as a regular Python program you can edit and run on `cslab`. If you like, you can install the necessary libraries (Jupyter, nltk, the nltk data described below) on your own computer and use this Jupyter notebook. Jupyter notebooks are really helpful for developing your code, and I highly recommend learning to use them! (It is possible to run a Jupyter notebook on a remote server using an ssh tunnel, but it's easier to just install nltk on your own computer.)

There are many tutorials and quick-start guides on the web for using Jupyter notebooks (<a href="https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/">here</a>, <a href="https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook">here</a>, <a href="http://bi1.caltech.edu/code/t0b_jupyter_notebooks.html">here</a>). Note that if you ever get weird behavior in a notebook. just go up to the Kernel menu and restart the kernel and clear the output, then run each code cell up to where you started having the problem.

Quick start: In the cell below, where it says <code> In [ ]: </code>, type <code>print("Hello, World!")</code>. Click in the cell below, and then hit the Run button from the menu of icons at the top of the page. Depending on your installation of jupyter, the run button might have the text Run or it might just be an icon that looks like a black triangle pointing to the right. The keyboard shortcut is <code>shift-return</code>, holding both keys down at the same time.



```python
print("Hello world!")
```

    Hello world!


Underneath your command you should now see the output <code>Hello, World!</code>. 

Great! Now you have run your first command in this Jupyter Notebook. You can always go back and edit the stuff you've written in any code cell. Just remember to re-run it if you change anything. 

*Note: Many jupyter beginners forget that if you change the value of some variable in a block of code, that variable now has that new value everywhere -- even in earlier blocks of code. If you are having trouble, it often helps to go back and re-run the block of code where you originally set the value of that variable.* 


## 1. Installing and configuring NLTK

Now let's start using nltk. The first thin you need to do is install the nltk library. If you're on cslab, you should know the drill by now

```
python3 -m pip install --user nltk
```

On your own computer you can leave out `--user`. 

You will additionally need to download some models and data. The easiest way to do it is to launch the **Python interactive terminal** (repl). Here's how to do that in a terminal cslab:

```
python3
```

This will give you a Python command line, where the prompt is `>>>`. Now type these two commands, one at a time:

```
import nltk
nltk.download('popular')
```

A bunch of stuff will get downloaded. Then you can quit the Python terminal like this:

```
quit()
```

## 2. Starting to use NLTK

First you need to import the library. Let's import `re` too since regular expressions are always helpful.


```python
# enter your import nltk command here and hit Run
import nltk
import re

```

We're going to look at Great Expectations, by Charles Dickens. Download this from Gutenberg using `curl` like this from the commandline.

```
curl https://www.gutenberg.org/files/1400/1400-0.txt > greatexpectations.txt
```

Now you have a text to work with. Using your preferred text editor, have a look at the file, and familiarize yourself with the format.

## 3. Loading in the text

You'll notice that plain text Gutenberg Project books are formatted to have 80 or fewer characters per line. This is fine for reading on an old-timey computer screen, but when we're processing text, we don't want a lot of manually inserted hard line breaks in the middle of our text. We're going to read in the text and replace line breaks with spaces. Run the code below.


```python
f = open("greatexpectations.txt", encoding="utf=8")
fulltext = f.read()
alltext = re.sub("\n", " ", fulltext)
```

<code>alltext</code> is a single string containing the entire text of the book. You can see that this is true by printing out the whole thing, but that will take up lots of space. Instead just try printing the first and last bunch of characters.


```python
print(alltext[:25])
print(alltext[-99:])
```

    ﻿The Project Gutenberg eB
    p produce our new eBooks, and how to subscribe to our email newsletter to hear about new eBooks.   


Recall from when you examined the file in a text editor that there there was a bunch of text at the beginning and end of the file that was not actually a part of the text of the book. Above I showed how to use <code>re.sub</code> to remove all the line breaks. In the cell below, use <code>re.sub</code> to delete everything up to and including ``Chapter I.   `` **followed by three spaces**. Then use <code>re.sub</code> to delete everything starting from the white space that appears before ``*** END OF THE PROJECT GUTENBERG EBOOK GREAT EXPECTATIONS ***`` all the way to the end of the file. 

Hint: Be very careful about spaces, case, punctuation, etc. Some regular expressions you will find very useful: <code>+ ^ $ \s .\*</code> and <code>.\*?</code> and the backslash.


```python
alltext = re.sub("^.*?Chapter I\.\s\s\s", "", alltext)
alltext = re.sub("\s+\*\*\* END OF THE.*?$", "", alltext)
print(alltext[:25])
print(alltext[-99:])
```

    My father’s family name b
    the broad expanse of tranquil light they showed to me, I saw no shadow of another parting from her.


If you did your regular expressions right, repeating the slice printing commands above will yield the following output:

<code>My father’s family name b</code><br> 
<code>the broad expanse of tranquil light they showed to me, I saw no shadow of another parting from her.</code>

<b>If you didn't get this output, *go back and reload the file* by putting the cursor in the command cell where you originally read in the file and clicking Run.</b> Then try your regular expression again. Do not continue until you get the right output.

## 4. Word tokenization

In Python, you can turn a "sentence" into a string of "words" by splitting on white space using the <code>split</code> function. As we've discussed in class, however, splitting on white space is not a great way to tokenize (i.e., to separate out each actual word-like unit) because you leave punctuation attached to words. This prevents you from recognizing that, for instance, "dogs" is the same word whether it's before a space or a comma. In addition, you won't be able to learn anything about the distribution of different punctuation marks since they will always be attached to something else.

Fortunately, nltk has a word tokenizer function that, when given a string, will return a list of tokens. Here's the syntax for calling it:

<code>listoftokens = nltk.word_tokenize(inputstring)</code>

Call this function on <code>alltext</code> to produce a list of tokens called <code>alltokens</code>. 
 


```python
# call nltk.word_tokenize here and Run
alltokens = nltk.word_tokenize(alltext)

```

### <b>Q1: How many tokens are there in this text? How many types are there in this text? What is the type:token ratio? Write three python commands in the line below that will calculate these three numbers. Then print out all three numbers.
 </b>


```python
# line of code for token count

numtokens = len(alltokens)
print(numtokens)

# line of code for type count

numtypes = len(set(alltokens))
print(numtypes)

# line(s) of code for type:token ratio
print(numtypes/numtokens)

print(alltokens[:100])

```

    225601
    13310
    0.05899796543455038
    ['My', 'father', '’', 's', 'family', 'name', 'being', 'Pirrip', ',', 'and', 'my', 'Christian', 'name', 'Philip', ',', 'my', 'infant', 'tongue', 'could', 'make', 'of', 'both', 'names', 'nothing', 'longer', 'or', 'more', 'explicit', 'than', 'Pip', '.', 'So', ',', 'I', 'called', 'myself', 'Pip', ',', 'and', 'came', 'to', 'be', 'called', 'Pip', '.', 'I', 'give', 'Pirrip', 'as', 'my', 'father', '’', 's', 'family', 'name', ',', 'on', 'the', 'authority', 'of', 'his', 'tombstone', 'and', 'my', 'sister', ',', '—Mrs', '.', 'Joe', 'Gargery', ',', 'who', 'married', 'the', 'blacksmith', '.', 'As', 'I', 'never', 'saw', 'my', 'father', 'or', 'my', 'mother', ',', 'and', 'never', 'saw', 'any', 'likeness', 'of', 'either', 'of', 'them', '(', 'for', 'their', 'days', 'were']


### <b>Q2: What text normalization might you want to do before counting the number of types and tokens? (Hint: there are some words you might be counting as separate types because of the way they are spelled.) How might this normalization make your type and token counts more accurate? How might it make these counts less accurate?</b>

## 5. Frequency distributions

Your answers to Q1 demonstrate that there must be some words that were used more than once. Suppose you want to know what are the most frequent words. You can do this using the <code>FreqDist()</code> class in nltk. Run the code below to create a frequency distribution for your list of tokens and to print out the 10 most frequent words and their counts.


```python
fdist = nltk.FreqDist(alltokens)
print(fdist.most_common(10))
```

    [(',', 17046), ('the', 7746), ('and', 6597), ('I', 6543), ('.', 6470), ('to', 4999), ('of', 4385), ('“', 3945), ('”', 3908), ('a', 3892)]


It's not too surprising that the words you see in this list are the most common words. These little words that don't add a lot of content to language but appear frequently and usually serve a specific function are called <i><b>function words</i></b> or <i><b>closed class words</i></b>. These words are important, but the don't tell us much by themselves about the story.

What should we do if we want to know the most frequent words that are <i><b>content words</b></i> or <i><b>open class words</b></i> like nouns, verbs, adjectives, and adverbs -- the kinds of words that can tell us more about the story itself?

We filter out the function words using a <i><b>stop list</b></i>, which is a list of words that we can skip when we're interested in the real content of a text. nltk provides a stop list that you can use and add to. Let's get it and print it out to see what's there.


```python
from nltk.corpus import stopwords
```


```python
stoplist = stopwords.words("english")
print(stoplist)
```

    ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


### Q3: What common and important class of tokens is missing from this list that we also might like to ignore?

Add at least three of these missing tokens to the stop list using the usual Python syntax for appending to or extended a list, and check to make sure it worked. Then make a new version of <code>alltokens</code> from which all stop words in your stoplist have been removed. Finally, create a new <code>FreqDist</code> from this stopword-free list of tokens, and print out the top 10 tokens.

Keep adding stop words (or stop tokens!) to the stoplist until you start seeing mostly real content words in the top 10.

(Note: There are smart quotes in the text because it's UTF-8 not ascii. You can add these to the stoplist by just copying and pasting them into your list of things you're adding to the stoplist.)


```python
stoplist = stopwords.words('english')

# enter your code for appending at least three tokens to the stop list here
stoplist.extend([".", ",", "?", "could", "would", "“", "”", "’", ";", "!"])

# print out the stoplist to make sure your new tokens were added correctly
print(stoplist)

# make a new version of alltokens called allcontenttokens that doesn't contain items from the stop list
allcontenttokens = [w for w in alltokens if w.lower() not in stoplist]

# create a new FreqDist from this new version of alltokens
fdist = nltk.FreqDist(allcontenttokens)
fdist.most_common(20)


# print out the top 10 most frequent tokens in this new FreqDist


```

    ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", '.', ',', '?', 'could', 'would', '“', '”', '’', ';', '!']





    [('said', 1346),
     ('Joe', 726),
     ('Mr.', 677),
     ('one', 468),
     ('know', 372),
     ('Miss', 372),
     ('upon', 353),
     ('little', 350),
     ('time', 345),
     ('come', 339),
     ('looked', 323),
     ('Herbert', 311),
     ('Pip', 309),
     ('man', 309),
     ('Havisham', 306),
     ('like', 299),
     ('made', 298),
     ('went', 289),
     ('much', 289),
     ('never', 285)]



### Q4: How many tokens did you have to add to the stoplist? What do you think of nltk's stoplist?

## 6. Stemming and lemmatization

There's a common normalization task we haven't performed yet: stemming or lemmatization.

### Q5: Looking at the top 50 or 100 most frequent unigrams, how can you tell the tokens are not stemmed or lemmatized? 

The command cell below shows how to use nltk's only true lemmatizer, the WordNet Lemmatizer.


```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# an example
print(lemmatizer.lemmatize("men"))
print(lemmatizer.lemmatize("eats"))
```

    men
    eats


Use this lemmatizer to lemmatize every token in the <code>allcontenttokens</code> list you created above. Then make a new frequency distribution and examine the 50 or 100 most frequent words.

**Note: I want you to use ``allcontenttokens`` here. Why? Because we are thinking about words by themselves here rather than word sequences so we can disregard function words. In addition, you can lemmatize only verbs, nouns, adjectives, and adverbs (in English, at least).**


```python


# create a new list of tokens, alllemmas by lemmatizing allcontenttokens
all_lemmas = [lemmatizer.lemmatize(w) for w in allcontenttokens]


# build a new FreqDist and examine the 50 or 100 most frequent words
fdist = nltk.FreqDist(all_lemmas)
print(fdist.most_common(25))


fdist2 = nltk.FreqDist(allcontenttokens)
print(fdist2.most_common(25))


```

    [('said', 1346), ('Joe', 726), ('Mr.', 677), ('one', 475), ('hand', 444), ('time', 434), ('know', 396), ('Miss', 372), ('come', 357), ('upon', 353), ('little', 350), ('looked', 323), ('say', 322), ('Herbert', 311), ('Pip', 309), ('man', 309), ('Havisham', 306), ('like', 301), ('made', 298), ('went', 289), ('much', 289), ('way', 287), ('never', 285), ('Wemmick', 280), ('see', 273)]
    [('said', 1346), ('Joe', 726), ('Mr.', 677), ('one', 468), ('know', 372), ('Miss', 372), ('upon', 353), ('little', 350), ('time', 345), ('come', 339), ('looked', 323), ('Herbert', 311), ('Pip', 309), ('man', 309), ('Havisham', 306), ('like', 299), ('made', 298), ('went', 289), ('much', 289), ('never', 285), ('Wemmick', 280), ('say', 274), ('see', 271), ('way', 264), ('hand', 262)]


It probably doesn't look much better. This is because the WordNet lemmatizer in nltk assumes by default that every word is a noun. Unless you tell the lemmatizer that something is a verb, it won't try to look it up as a verb. This is why "said" doesn't get lemmatized, and also why "was" gets lemmatized to "wa". We will learn about how to find out a word's part of speech next week, which will make the stemmer work better.

Note that there are several different stemmers implemented in the nltk.stem package. You can explore these in the nltk.stem package.

Make sure you've answered every <b>Q</b> question.

Make sure you've written code wherever required. 

Go up to the Kernel menu and select Restart and Run All. **(Don't forget that you can comment out or skip the nltk download block and the urllib block.)** This will run all of the code you've written. Make sure there are no errors.

Add, commit, and push this file and the <code>great.txt</code> file to your repo. When you are totally done, make the comment say "FINAL SUBMISSION - PLEASE GRADE".


```python

```
