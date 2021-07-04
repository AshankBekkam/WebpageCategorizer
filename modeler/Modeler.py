import os
import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

class Modeler:
    def __init__(self):
        
        self.dataset = pd.read_csv('F:\Scalenut\modeler\cleaned_website_classification.csv')
        try:
            self.model = joblib.load('models/webclass.joblib')
        except:
            self.model = None
            self.count_vectorizer = None
            self.tfidf = None

    
    def fit(self):
        y=self.dataset['Category']
        X = self.dataset.drop(columns=['Category'])
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, stratify=y,random_state = 42)
        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', KNeighborsClassifier(n_neighbors=7)),
        ])
        text_clf.fit(X_train.cleaned_website_text, y_train)
        joblib.dump(text_clf,'models/webclass.joblib')
    
    def predict(self,text):
        if not os.path.exists('models/webclass.joblib'):
            raise Exception("Train model before making predictions")
        if(len(text)==0):
            raise Exception("No description is available")

        text_clf = joblib.load('models/webclass.joblib')
        predicted = text_clf.predict(text)
        return predicted













