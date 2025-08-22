"""
For visualizations
we are going to use libraries such as Matplotlib, Seaborn,
plotly, or Bokeh
"""

import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

data_path = ("C:/Users/titom/Downloads/test_examples.csv")
df = pd.read_csv(data_path)

#bar plot of the dataset representing overall toxicity messages within the dataset, the toxic side being on the left and the controlled variable (non toxic messages) being on the right

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
"""
Histo Plot showing the extremely toxic messages going all the way up, which is few and having the rest that are around mid toxicity represented as blue. 
"""

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
