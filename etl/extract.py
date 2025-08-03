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