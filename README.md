# Predicting Video Game Review Scores Using Tf-idf 

Video game reviews are either text or video based, and are often accompanied by a score, indicating the reviewer's overall opinion on the quality of the game.  I wanted to examine text based reviews, to see if I could build a model that predicts a review score based on text features.  I scraped 2,903 reviews from the video game website IGN.com to use as my corpus, along with the review score for each review.

## Data Exploration
IGN scores their reviews on a scale from 0-10, allowing for any value rounded to the first decimal.  Here are some basic summary statistics on the review scores:
```python
Out[107]:

count    2903.000000
mean        7.326628
std         1.499496
min         1.500000
25%         6.500000
50%         7.500000
75%         8.500000
max        10.000000
```
Along with the review scores and text, I scraped the genre of the game.  Action and Adventure are the most highly represented, followed by Shooter and RPG:

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Reviews%20Per%20Genre.png" height="300" width="145">

These reviews were written from 2010 to 2018.  The mean score has increased over time, while the number of reviews written has decreased:

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Average%20Review%20Score%20-%20Time.png" height="300" width="400">

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Number%20Reviews%20-%20Time.png" height="300" width="400">

The reviews were written for games across a variety of platforms, with PC as the mostly highly represented, followed by Playstation 3 and Playstation 4:

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Reviews%20Platform.png" height="300" width="145">

## Data Pre-Processing for Tf-idf


My models will be fit using the matrix as the feature and using the review score as the target.

In order to create an effective tf-idf, I performed the following pre-processing steps:
1)  Lowercase the text.  
2)  Removing brackets from beginning and end of documents
3)  Remove newline characters
4)  Remove punctuation
5)  Remove stopwords (using NLTK)
6)  Removed common and uncommon words
7)  Spelling correction (using textblob)
8)  Lemmatization

The primary purpose of these pre-processing steps is to clean the data set so that unhelpful characters are removed and the vocabulary of the corpus is refined. Words that are either rare or common will be removed from the dataset, as they most likely will only add unecessary noise to the model.  The steps of lowercasing, spelling correction, and lemmatization further reduce the number of unique words, as they remove redundancies from the corpus.

## Feature Creation


The primary feature I planned to use was a term frequency-inverse document frequency (tf-idf) representation of the corpus.  According to Wikipedia, "tf-idf is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus...The tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general".  I will represent the tf-idf in a matrix, with each unique document (in this case different review) in its own row, and each unique word in its own column.  

(INSERT EXAMPLE PHOTO)

Before creating the tf-idf, I split the dataset into a training and validation set.  I wanted to make sure the tf-idf that model is fit on was not influenced by the validation set.  There are a number of packages that exist to assist in the creation of a tf-idf.  I used the Gensim implementation, as I have found that it scales better than other implementations I have used.  Based on my cleaned training dataset, I used Gensim to create a dictionary, create a corpus, create a tf-idf, and apply the tf-idf to my corpus.  

```python
dictionary = corpora.Dictionary(texts)
dictionary.filter_extremes(no_below=5, no_above=0.6, keep_n=10000)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
```
I then followed the same steps for the validation set, with the exception of creating a tf-idf.  Instead I applied the tf-idf I created during from the training set to the validation corpus.  I then converted 

## Modeling

I wanted to try a couple of different types of machine learning algorithms to see what would work best to solve this problem.  The four approaches I settled on were a gradient boosted decision tree (using XGBoost), linear regression (OLS), Lasso regression, and a deep learning model with 5 fully-connected hidden layers (using Tensorflow).  Since I was trying to predict a continuous value, I used the regression implementations of XGBoost and Tensorflow.  The metric I decided to use to score my model was root mean square error (RMSE).  As a baseline, I computed the RMSE assuming I used the mean score for all reviews as the prediction.  Here are my cross-validated results:

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Results.png" height="125" width="400">

All models outperformed the baseline by at least 30%, indicating that machine learning models built using a tf-idf representation had some predictive ability.  

The deep learning and gradient boosted decision tree implementations that I used were fairly vanilla, and could probably be improved with additional experimentation.

## Additional Experiments

In addition to using the tf-idf as the input into the model, I tried incorporating several other features, to see if I could improve performance.  I created a topic model using latent Dirichlet allocation and built a predictive model based on the output of the topic model.  This model had almost zero predictive value.  I also built a model using only the genre of the game to predict performance. This also had minimal predictive value.  I experimented with 2 and 3 word n-grams to build the tf-idf.  This added extra noise to the model and preformed worse than a single word tf-idf. 

## Future Work

One shortcoming of a tf-idf is that semantic meaning is lost while using this representation.  While a model built using tf-idf does have predictive power, it may be the case that models built upon other features would perform better.  In particular, using learned word embeddings would be an interesting avenue for future exploration.  

# Description of Python files and Jupyter notebooks:

Exploration and model testing.ipynb-includes exploration and best performing models using TF-IDF

Model using genre.ipynb-model built using genre as only feature

Model using genre to adjust final pred.ipynb-model with final predictions being adjusted by genre

Model using n-gram.ipynb-model TF-IDF built using n-grams as features

Model using topic models.ipynb-model with topic model as features

scrapereviewlinks.py-code to scrape links to reviews

scrapereviewpage.py-code to scrape text from review page


