# sys6018-final-project

Description of Python files and Jupyter notebooks:

Exploration and model testing.ipynb-includes exploration and best performing models using TF-IDF

Model using genre.ipynb-model built using genre as only feature

Model using genre to adjust final pred.ipynb-model with final predictions being adjusted by genre

Model using n-gram.ipynb-model TF-IDF built using n-grams as features

Model using topic models.ipynb-model with topic model as features

scrapereviewlinks.py-code to scrape links to reviews

scrapereviewpage.py-code to scrape text from review page



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

My goal was to build a model based primarily on a term frequency-inverse document frequency (tf-idf) representation of the corpus.  According to Wikipedia, "tf-idf is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus...The tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general".  We will represent the tf-idf in a matrix, with each unique document (in this case different review) in its own row, and each unique word in its own column.  

(INSERT EXAMPLE PHOTO)

The goal of the tf-idf representation will be to create 


I needed to prepare the raw text that I downloaded so it was formatted correctly.  




