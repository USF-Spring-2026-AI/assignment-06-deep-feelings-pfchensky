import pandas as pd
import numpy as np
import spacy

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# load data
train_df = pd.read_csv("A06_train.csv", header=None, names=["label", "text"])
test_df = pd.read_csv("A06_test.csv", header=None, names=["label", "text"])

# assign text column to train_x, test_x and label column to train_y,test_y
train_x = train_df["text"]
train_y = train_df["label"]

test_x = test_df["text"]
test_y = test_df["label"]

# create a spacy model
model = spacy.load("en_core_web_md")

# a helper function to convert text to embedding features
def get_vectors(texts):
    vectors = []

    for text in texts:
        doc = model(text)
        vectors.append(doc.vector)

    return np.vstack(vectors)

# convert text into spacy embedding features
train_x_vectors = get_vectors(train_x)
test_x_vectors = get_vectors(test_x)

# create a logistic regression model
lr = LogisticRegression(max_iter=1000)

# using training data to train model
lr.fit(train_x_vectors, train_y)

# predict and calculate accuracy
print("Embeddings Accuracy:", accuracy_score(test_y, lr.predict(test_x_vectors)))