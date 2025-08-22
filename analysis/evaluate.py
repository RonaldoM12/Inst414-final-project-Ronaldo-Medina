# """
# In evaluate we are going to use measures such as 
# accuracy, and recall in order to get the model used to
# seeing potential scenarios
# """

# import logging
# from typing import Dict, Iterable, Optional
# import numpy as np
# import pandas as pd
# from sklearn.metrics import (
#     accuracy_score, 
#      recall_score,
#      precision_score,
#      f1_score,
#      confusion_matrix,
#      roc_auc_score
#      )

# logger = logging.getLogger(__name__)

# """
# An evaluation class that will look at accuracy, recalling
# precision and f1, we also have logging which will start at the 
# very beggining and just before the value is returned it will output finish

# """
# def evaluation_class(y : Iterable[int], y_guess: Iterable[int], y_probability: Optional[Iterable[float]] = None) -> Dict[str, float]:
#     logger.info('Started')
#     y = np.asarray(list(y))
#     y_guess = np.asarray(list(y_guess))

#     measures = {
#         "accuracy": accuracy_score(y, y_guess),
#         "recall" : recall_score(y, y_guess, pos_label=1, zero_division= 0),
#         "precision": precision_score(y, y_guess, pos_label=1, zero_division = 0),
#         "f1": f1_score(y, y_guess, pos_label = 1, zero_division= 0),
#     }

#     if y_probability is not None:
#         y_probability = np.asarray(list(y_probability))
#         measures["roc_auc"] = roc_auc_score(y, y_probability)

    
#     matrix = confusion_matrix(y, y_guess)
#     measures["confusion_matrix"] = {
#         "tn": int(matrix[0,0]), "fp": int(matrix[0,1]),
#         "fn": int(matrix[1,0]), "tp": int(matrix[1,1])
#     }

#     # if accuracy_score == 0:
#     #     print("This is a non toxic message and you may continue")
#     # elif accuracy_score <= 0.33:
#     #     print("This message has a keyword which is identified as toxic")
#     # elif accuracy_score <= 0.5:
#     #     print("At minimum half of this message is toxic and needs to be reviewed")
#     # elif accuracy_score == 0.75:
#     #     print("The majority of this message needs to be revised and cannot be sent")
#     # else:
#     #     print("This message is extremely toxic and WILL NOT be sent, this message is now pending review")

    
#     logger.info('Finished')
#     print(measures)
#     return measures
