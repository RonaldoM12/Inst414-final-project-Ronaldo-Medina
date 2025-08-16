"""
For Extract
I am going to be pulling data from both riot API and 
IBM Toxic Classifier dataset which helps identify key words which
are constantly being used 
This is going to be saved as either CSV's or JSON Formats

"""

"""
Psuedo code:

I am going to use logistic regression 
I am going to have a function
def pulling_data():
data_path = "riot_API.csv)
data = pd.read_csv(data_path)

x = data['comment_text']
y = data['toxic']

data variables that can split the load

w_data, x_data, y_data, z_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

create a "pipeline"

then return the pipeline
"""
import os, re, logging
import mylib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
logger = logging.getLogger(__name__)

"""
Both funcitons extract the CSVs one from riot and the other from
IBM, IBM has 4 seperate data formats I will be using train as it 
is the dataset which contains the toxicity comments
"""

def extractRIOT(data_path = "riot_API.csv"):
    logger.info('Started')
    
    data = pd.read_csv(data_path)

    x = data["comment_text"].astype(str)
    y = data["toxic"].astype(str)

    W, A, S, D = train_test_split(
        x, y, test_size= 0.9, random_state= 50, stratify= y
    )
    
    pipeline = Pipeline()

    pipeline.fit(x,y)
    print("Accuracy", pipeline.score(x,y))
    
    logger.info('Finished')

    return pipeline


def extractIDM(data_path = "train.csv"):
    logger.info('Started')

    data = pd.read_csv(data_path)

    x = ["severe_toxic", "Obscene"].astype(str)
    y = ["threat","insult","identity_hate"].astype(str)

    W, A, S, D = train_test_split(
        x, y, test_size= 0.9, random_state= 50
    )

    pipeline = Pipeline()

    pipeline.fit(x,y)
    print("IBM Accuracy: ", pipeline.score(x,y))

    logger.info('Finished')

    return pipeline



