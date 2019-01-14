# sys6018-final-project

Description of Python files and Jupyter notebooks:

Exploration and model testing.ipynb-includes exploration and best performing models using TF-IDF

Model using genre.ipynb-model built using genre as only feature

Model using genre to adjust final pred.ipynb-model with final predictions being adjusted by genre

Model using n-gram.ipynb-model TF-IDF built using n-grams as features

Model using topic models.ipynb-model with topic model as features

scrapereviewlinks.py-code to scrape links to reviews

scrapereviewpage.py-code to scrape text from review page



# Predicting Video Game Review Scores Using TFIDF 

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

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Reviews%20Per%20Platform.png" height="300" width="145">

These reviews were written from 2010 to 2018.  The mean score has increased over time, while the number of reviews written has decreased:

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Average%20Review%20Score%20-%20Time.png" height="300" width="400">

<img src="https://github.com/swgleave/sys6018-final-project/blob/master/images/Number%20Reviews%20-%20Time.png" height="300" width="400">

The reviews were written for games across a variety of platforms, with PC as the mostly highly represented, followed by Playstation 3 and Playstation 4:


