import pandas as pd
import matplotlib.pyplot as plt
# Exactly the same as the code in question 4, see question 4 for comments and explanations
def plot_rating(csv_filename,version_label_model):
    df=pd.read_csv(csv_filename)
    df['date']=pd.to_datetime(df['date'],format='%Y-%m-%d',errors='coerce')
    df=df.sort_values(by='date')
    print(df['rating'])
    df['reviewVersion']=pd.to_numeric(df['reviewVersion'],errors='coerce')
    df['rating']=pd.to_numeric(df['rating'],errors='coerce')
    max=0
    for index, row in df.iterrows():
        if row['reviewVersion']>max:
            max=row['reviewVersion']
        else:
            df.loc[index:index,('reviewVersion')]=None
    sum=0
    n=0
    aver=[]
    year=[]
    df=df.dropna(subset=['date'])
    for index, row in df.iterrows():
        initial_date_index=index
        break
    t1=df.loc[initial_date_index,'date']
    for index, row in df.iterrows():
        t = row['date']
        n=n+1
        sum=sum+row['rating']
        if (t.month-t1.month!=0)and(t.month!=None):
            a = sum / n
            print(a)
            aver.append(a)
            year.append(row['date'])
            n = 1
            t1 = t
            sum = row['rating']
            print(row['date'])
    plt.plot(year, aver)
    max = 0
    k=0
    if version_label_model == 0:
        for index, row in df.iterrows():
            if row['reviewVersion'] > max:
                max = row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1])) <= 1:
                    plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=8,
                             verticalalignment='bottom', rotation=45)
                    plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
    if version_label_model == 1:
        for index, row in df.iterrows():
            sum=sum+row['rating']
            if row['reviewVersion']>max:
                max=row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1]))<=1:
                    k=k+1
                    if (k%2==0):
                        plt.text(row['date'], plt.axis()[3],'Version:'+str(row['reviewVersion']),fontsize=6,
                                 verticalalignment='bottom',rotation=38)
                        plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    else:
                        plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=6,
                                 verticalalignment='top', rotation=-38)
                        plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    print(row['reviewVersion'])
    plt.show()

def plot_sentiment(csv_filename,version_label_model):
    df=pd.read_csv(csv_filename)
    df['date']=pd.to_datetime(df['date'],format='%Y-%m-%d',errors='coerce')
    df['reviewVersion']=pd.to_numeric(df['reviewVersion'],errors='coerce')
    df=df.sort_values(by='date')
    max=0
    for index, row in df.iterrows():
        if row['reviewVersion']>max:
            max=row['reviewVersion']
        else:
            df.loc[index:index,('reviewVersion')]=None
    sum=0
    n=0
    aver=[]
    year=[]
    df=df.dropna(subset=['date'])
    for index, row in df.iterrows():
        initial_date_index = index
        break
    t1=df.loc[initial_date_index,'date']
    for index, row in df.iterrows():
        t = row['date']
        n=n+1
        sum=sum+row['compound']
        if (t.month-t1.month!=0)and(t.month!=None):
            a = sum / n
            print(a)
            aver.append(a)
            year.append(row['date'])
            n = 1
            t1 = t
            sum = row['compound']
            print(row['date'])
    plt.plot(year, aver)
    max=0
    k=0
    if version_label_model==0:
        for index, row in df.iterrows():
            if row['reviewVersion'] > max:
                max = row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1])) <= 1:
                    plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=8,
                             verticalalignment='bottom', rotation=40)
                    plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    print(row['reviewVersion'])
    if version_label_model==1:
        for index, row in df.iterrows():
            if row['reviewVersion']>max:
                max=row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1]))<=1:
                    k = k + 1
                    if (k % 2 == 0):
                        plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=6,
                                 verticalalignment='bottom', rotation=38)
                        plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    else:
                        plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=6,
                                 verticalalignment='top', rotation=-38)
                        plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    print(row['reviewVersion'])
    plt.show()

plot_sentiment('parkman/attitude.csv',0)
plot_sentiment('parkman/behavioral intentions.csv',0)
plot_sentiment('parkman/perceived usefulness.csv',0)
plot_sentiment('parkman/perceived ease of use.csv',0)
plot_sentiment('parkman/satisfaction.csv',0)

plot_rating('parkman/attitude.csv',0)
plot_rating('parkman/behavioral intentions.csv',0)
plot_rating('parkman/perceived usefulness.csv',0)
plot_rating('parkman/perceived ease of use.csv',0)
plot_rating('parkman/satisfaction.csv',0)

plot_sentiment('easypark/attitude.csv',1)
plot_sentiment('easypark/behavioral intentions.csv',1)
plot_sentiment('easypark/perceived usefulness.csv',1)
plot_sentiment('easypark/perceived ease of use.csv',1)
plot_sentiment('easypark/satisfaction.csv',1)

plot_rating('easypark/attitude.csv',1)
plot_rating('easypark/behavioral intentions.csv',1)
plot_rating('easypark/perceived usefulness.csv',1)
plot_rating('easypark/perceived ease of use.csv',1)
plot_rating('easypark/satisfaction.csv',1)
