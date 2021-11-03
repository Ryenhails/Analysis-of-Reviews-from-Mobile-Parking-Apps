from sklearn.model_selection import train_test_split
import os,re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from nltk.corpus import stopwords
from numpy import *
import sys
# Save the contents of print to TXT
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

sys.stdout = Logger('result.txt')

# Merge two Dataframes
df1 = pd.read_csv('randomforest_data/parkmano.csv',sep = ';')
df2 = pd.read_csv('randomforest_data/easyparko.csv',sep = ';')
df = pd.concat([df1,df2],axis=0,ignore_index=True)

def ngram_randomforest(Dataframename,Ngram_number,Ngram_feature_size,estimators,test_size,topimportance_element_number):
    # Clean data: drop stopwords, punctuation, capital letters
    eng_stopwords = stopwords.words('english')
    def clean_text(text):
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        words = text.lower().split()
        words = [w for w in words if w not in eng_stopwords]
        return ' '.join(words)
    df['clean_review'] = Dataframename.content.apply(clean_text)
    df.head()

    # Use CountVectorizer to generate N-Gram
    vectorizer_gram = CountVectorizer(ngram_range=Ngram_number,token_pattern=r'\b\w+\b',max_features=Ngram_feature_size)
    # convert n-gram to feature data
    train_vsm_gram = vectorizer_gram.fit_transform(df.clean_review).toarray()
    # split dataset as Training dataset and Test dataset
    X_train,X_test,y_train,y_test = train_test_split(train_vsm_gram,df.sentiment,test_size=test_size,stratify=df.sentiment)
    #print("top 10 n-gram elements：\n")
    #print(vectorizer_gram.get_feature_names()[:10])
    # Set up RandomForest model and train model
    forest = RandomForestClassifier(oob_score=True,n_estimators = estimators)
    forest = forest.fit(X_train, y_train)

    # Evaluate RandomForest model
    print("\n====================evaluate==================\n")

    def model_eval(test_x,test_y):
        print("1、metrics：\n")
        print(metrics.confusion_matrix(test_y, forest.predict(test_x)))

        print("\n2、precision recall f1-score：\n")
        print(metrics.classification_report(test_y, forest.predict(test_x)))

        print("\n3、oob_score：\n")
        print(forest.oob_score_)
    model_eval(X_test, y_test)

    # N-gram evaluate and use the trained model to classify the features
    print("\n====================n-gram evaluate==================\n")
    b=vectorizer_gram.get_feature_names()
    dff = pd.DataFrame({'f':b})
    f_s = vectorizer_gram.fit_transform(dff.f).toarray()
    classify=forest.predict(f_s)
    sorted_idx = argsort(-forest.feature_importances_)
    print('\nThe top ',topimportance_element_number,'elements, their importance number and class\n')
    n=0
    for i in sorted_idx:
        print(vectorizer_gram.get_feature_names()[i], forest.feature_importances_[i],classify[i])
        n=n+1
        if n==topimportance_element_number:
            break
    print('\nThe complete list of elements\' importance number and class\n')
    for i in sorted_idx:
        print(vectorizer_gram.get_feature_names()[i], forest.feature_importances_[i],classify[i])
    print('\nThe print result is saved as txt\n')


ngram_randomforest(df, (2,3), 500, 200, 0.3,10)
# ngram_randomforest(Dataframename, Ngram_number, Ngram_feature_size, estimators, test_size, show_ngram_number)