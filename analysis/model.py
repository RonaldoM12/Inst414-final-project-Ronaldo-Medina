"""
in model, we are going to design it with the intention
of using Logistic Regression in order to compute all of the
calculations
"""
import logging
import mylib
from typing import Dict, Iterable, Optional
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer as vector
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
logger = logging.getLogger(__name__)

"""
This code is only partially complete as there were complications 
so I removed those lines of code and left this currently
"""

def model(
        col: Optional[str] = "comment_text",
        num_cols: Optional[list[str]] = None,
        max = 2,
        float = 1.0,
        max_iter = 200) -> Pipeline:
    logger.info('Started')
    lists = []

    if col is not None:
        lists.append((
            "text",
            vector(
                ngram_range = (1, max),
                lowercase = True,
                strip_accents = "unicode",
                sublinear_tf = True,
                min_df = 2
            ),
            col
        ))

                    
        
    if num_cols:
        lists.append(("num",
                       Pipeline([
                           ("impute", SimpleImputer(strategy="median"))
                           ("scale", StandardScaler())
                       ])))
        
    logger.info('Finished')
    return lists

