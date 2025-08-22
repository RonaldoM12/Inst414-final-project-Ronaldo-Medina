from analysis.model import evaluation_class
from etl.extract import extractIDM
from etl.transform import loadCsv
from vis.visualizations import figurePlotter, histoPlotter

"importing all of the folders"
"in order to call upon the python files within"

"""Main will be the main function that we call upon in order
to run all of our code as well as periodically testing
it"""
def main():
    
    ev = evaluation_class([0,0,0,0,0,0], [0,1,1,1,0,1])
    elIDM = extractIDM('data/test_examples.csv')
    tmLOAD = loadCsv()
    vsfigure = figurePlotter()
    vshisto = histoPlotter()

"""the purpose of this code is to run and call upon our main
funtion to execute """
if __name__ == "__main__":
    main()