import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('data.csv')

### Data Exploration ###

print(data.info())
print(data.head())


### Data Cleaning ###
data.dropna(inplace=True)

# the data set is encoded like M = malinignant and B = benign tsma we need to encode it to 0 and 1
le = LabelEncoder()
data['diagnosis'] = le.fit_transform(data['diagnosis'])
