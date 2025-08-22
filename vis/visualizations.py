"""
For visualizations
we are going to use libraries such as Matplotlib, Seaborn,
plotly, or Bokeh
"""
import bokeh
import logging
import plotly
import re
import pandas as pd
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

data_path = ("C:/Users/titom/Downloads/test_examples.csv")
df = pd.read_csv(data_path)

def figurePlotter():

    logger.info('Started')

    plt.figure(figsize=(8, 5))
    sns.countplot(x="toxic", hue="toxic" , data= df, palette = "coolwarm")
    plt.xlabel("Toxicity")
    plt.ylabel("toxic measured")
    plt.savefig("ToxicityCounter.png")
    plt.show()

    logger.info('Finished')

    return plt

def histoPlotter(y = df):

    logger.info('Started')

    plt.figure()
    plt.hist(y, bins= 10)
    plt.xlabel("Toxicity")
    plt.ylabel("Toxic measured")
    plt.savefig("ToxicIndicator.png")
    plt.show()

    logger.info('Finished')

    return plt
