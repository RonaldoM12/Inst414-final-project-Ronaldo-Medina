"""
For visualizations
we are going to use libraries such as Matplotlib, Seaborn,
plotly, or Bokeh
"""
import bokeh
import logging
import mylib
import plotly
import re
import pandas as pd
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def figurePlotter():

    logger.info('Started')

    plt.figure(figsize=(8, 5))
    sns.countplot(x="Toxic", data=sample_submission, palette = "coolwarm")
    plt.title("Countering Toxicity")
    plt.xlabel("Toxicity")
    plt.ylabel("Balancing")
    plt.savefig("ToxicityCounter.png")
    plt.show()

    logger.info('Finished')

    return plt

def histoPlotter(y):

    logger.info('Started')

    plt.figure()
    plt.hist(y, bins= 20)
    plt.xlabel("Predicted Toxicity")
    plt.ylabel("Counter")
    plt.title("")
    plt.savefig("")
    plt.show()

    logger.info('Finished')

    return plt

"""
another plot
def histoPlotter(y):

    logger.info('Started')

    plt.figure()
    plt.hist(y, bins= 20)
    plt.xlabel("Predicted Toxicity")
    plt.ylabel("Counter")
    plt.title("")
    plt.savefig("")
    plt.show()

    logger.info('Finished')

    return plt
"""

"""
a different plot 
def histoPlotter(y):

    logger.info('Started')

    plt.figure()
    plt.hist(y, bins= 20)
    plt.xlabel("Predicted Toxicity")
    plt.ylabel("Counter")
    plt.title("")
    plt.savefig("")
    plt.show()

    logger.info('Finished')

    return plt
"""
