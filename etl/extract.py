
import os, logging
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

logger = logging.getLogger(__name__)

"""
Both funcitons extract the CSVs one from riot and the other from
IBM, IBM has 4 seperate data formats I will be using train as it 
is the dataset which contains the toxicity comments
"""

#save into the data folder
# Extracts arrest data CSVs into dataframes

import os
import pandas as pd

# Create 'data' directory if it doesn't exist
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

url = "https://raw.githubusercontent.com/IBM/MAX-Toxic-Comment-Classifier/refs/heads/master/samples/test_examples.csv"

# Load datasets
df = pd.read_csv(url)

# Save data frames to `data/`
df.to_csv('data/test_examples.csv', index=False)
   
def extractIDM(data_path = "test_examples.csv"):
    logger.info('Started')

    
    x = df["comment_text"]
    y = df["toxic"].astype(int)

    W, A, S, D = train_test_split(
        x, y, test_size= 0.2, random_state= 50
    )

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(W, S)
    print("Toxicity: ", pipeline.score(A,D))

    logger.info('Finished')

    return pipeline



