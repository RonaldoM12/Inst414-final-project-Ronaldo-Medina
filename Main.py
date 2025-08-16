import analysis
import Data
import etl
import vis

import logging
import mylib
logger = logging.getLogger(__name__)
"importing all of the folders"
"in order to call upon the python files within"

"""Main will be the main function that we call upon in order
to run all of our code as well as periodically testing
it"""

def do_something():
    logger.info('Doing something')

def main():
    logging.basicConfig(filename='myapp.log', level= logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')


"""the purpose of this code is to run and call upon our main
funtion to execute """
if __name__ == "__main__":
    main()

