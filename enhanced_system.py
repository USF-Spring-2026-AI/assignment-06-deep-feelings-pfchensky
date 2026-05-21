import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
train_df = pd.read_csv("A06_train.csv", header=None, names=["label", "text"])
test_df = pd.read_csv("A06_test.csv", header=None, names=["label", "text"])


# assign text column to train_x, test_x and label column to train_y,test_y
train_x = train_df["text"]
train_y = train_df["label"]

test_x = test_df["text"]
test_y = test_df["label"]

# Enhanced System: remove stopwords && use unigram + bigram features
count_vect = CountVectorizer(stop_words="english",ngram_range=(1, 2))

# convert to word count features
train_x_counts = count_vect.fit_transform(train_x)
test_x_counts = count_vect.transform(test_x)

# create a logistic regression model
lr = LogisticRegression(max_iter=1000)

# using training data to train model
lr.fit(train_x_counts, train_y)

# predict and calculate accuracy
print("Enhanced System Accuracy:", accuracy_score(test_y, lr.predict(test_x_counts)))