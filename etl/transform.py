"""
In transform
I am going to transform the data taken and clean the text
watching out for how often words are being used
how often toxic keywords are coming out
do we have games where we do good and bad? is this consistent?
is there inconsistencies in how often you are doing bad?
are we doing bad every game? what are we scoring? 
and we are also taking into account the amount of times this 
user has been reported

than we are going to save this. 
"""
import logging
import mylib
import os, re, logging
import pandas as pd

"Helpers"
IBM_path = "data/ibm_toxic.csv"
RIOT_path = "data/riot_API.csv"
url = re.compile(r"(https?://\S+|www\.\S+)")
mentions = re.compile(r"@\w+")
hashtag = re.compile(r"#(\w+)")

logger = logging.getLogger(__name__)

"Cleans the taken datasets from any capitalization to "
"make sure it is scanning for the correct words"
def loadCsv():
    logger.info('Started')

    RIOT_path = pd.read_csv("riot_API.csv")
    IBM_path = pd.read_csv("train.csv")

    logger.info('Finished')
    
    return None

def cleanData(RIOT_path, IBM_Path):

    logger.info('Started')

    lower = lower.strip().lower()
    lower = url.sub(" ", lower)
    lower = mentions(" ", lower)
    lower = hashtag(lambda r: f"{r.group(1)}", lower)

    logger.info('Finished')

    return lower.strip()



