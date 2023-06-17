
# coding: utf-8
#Same modeling, slightly different code with similar results

# In[1]:

#Import libraries
import pandas as pd
import numpy as np
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import string 
from nltk.stem import WordNetLemmatizer
import csv







import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import joblib



df=pd.read_csv('new_cleaned_data.csv', index_col=0)

texts = df['new_text'].astype(str)
y = df['is_offensive']

vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)
X = vectorizer.fit_transform(texts)

loaded_model = joblib.load(open("svm.pkl", 'rb'))

# d=vectorizer.transform(["dat bird bitch heavy birdcage bitch byyyyyyrrrrrrrrrrrrr bitch"])


def run2(c):
    result=[]
    d=vectorizer.transform([c])
    ans=loaded_model.predict(d)
    if ans[0]==0:
        result.append("Normal")
        return result
    else:
        result.append("Hate")
        return result
    