import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# The common words comparison function, if they have word in common, then return 1
def compare(list1,list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return 1
    return 0
from nltk.corpus import wordnet
import nltk
nltk.download('averaged_perceptron_tagger')
#map the treebank tags to WordNet part of speech names:
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
# Merge two Dataframes
df1 = pd.read_csv('parkman.csv',sep = ';')
df2 = pd.read_csv('easypark.csv',sep = ';')
df = pd.concat([df1,df2],axis=0,ignore_index=True)

# Read keywords dataframe for 5 indicators
kw=pd.read_csv('extensionKeywords.csv',sep=';')


# Dealing with capital letters and punctuation
df['content'] = df['content'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['content'] = df['content'].str.replace('[^\w\s]',"")

# Create 5 dataframes for each indicator
peofd=pd.DataFrame(columns = df.columns.to_list())
pud=pd.DataFrame(columns = df.columns.to_list())
satd=pd.DataFrame(columns = df.columns.to_list())
attd=pd.DataFrame(columns = df.columns.to_list())
bid=pd.DataFrame(columns = df.columns.to_list())

# Create lists of keywords for each indicator
peof=kw.loc[0,('keywords')].split(',')
pu=kw.loc[1,('keywords')].split(',')
sat=kw.loc[2,('keywords')].split(',')
att=kw.loc[3,('keywords')].split(',')
bi=kw.loc[4,('keywords')].split(',')

# keywords cleaning
def keywordcleaning(list,new_list):
    lemmatizer = WordNetLemmatizer()
    list=nltk.pos_tag(list)
    for word ,tag in list:
        wntag = get_wordnet_pos(tag)
        if wntag is None:  # not supply tag in case of None
            new_list.append(lemmatizer.lemmatize(word))
        else:
            new_list.append(lemmatizer.lemmatize(word,wntag))

peof_clean=[]
pu_clean=[]
sat_clean=[]
sat_clean=[]
att_clean=[]
bi_clean=[]

keywordcleaning(peof,peof_clean)
keywordcleaning(pu,pu_clean)
keywordcleaning(sat,sat_clean)
keywordcleaning(att,att_clean)
keywordcleaning(bi,bi_clean)

# Classify
lemmatizer = WordNetLemmatizer()
for index, row in df.iterrows():
    temp=nltk.word_tokenize(row['content'])
    After_lem=[]
    temp=nltk.pos_tag(temp)
    for word ,tag in temp:
        wntag = get_wordnet_pos(tag)
        if wntag is None:  # not supply tag in case of None
            After_lem.append(lemmatizer.lemmatize(word))
        else:
            After_lem.append(lemmatizer.lemmatize(word,wntag))
        # Apply Lemmatization
    if compare(After_lem, peof_clean)==1:
        peofd.loc[index]=row
    if compare(After_lem, pu_clean) == 1:
        pud.loc[index]=row
    if compare(After_lem, sat_clean) == 1:
        satd.loc[index]=row
    if compare(After_lem, att_clean) == 1:
        attd.loc[index]=row
    if compare(After_lem, bi_clean) == 1:
        bid.loc[index]=row

# Save the csvfile
peofd.to_csv('indicators/perceived ease of use.csv',index=None)
pud.to_csv('indicators/perceived usefulness.csv',index=None)
satd.to_csv('indicators/satisfaction.csv',index=None)
attd.to_csv('indicators/attitude.csv',index=None)
bid.to_csv('indicators/behavioral intentions.csv',index=None)

