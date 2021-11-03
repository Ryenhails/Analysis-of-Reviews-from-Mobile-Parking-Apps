import pandas as pd
import matplotlib.pyplot as plt
def plot_sentiment(csv_filename,version_label_model):
    # csv_filename=filename
    # version_label_model=0,1(0 means Parallel label and 1 means Interlaced label)
    df=pd.read_csv(csv_filename,sep = ';')
    # convert object(date,version) to datatime and numeric
    df['date']=pd.to_datetime(df['date'],format='%Y-%m-%d',errors='coerce')
    df['reviewVersion']=pd.to_numeric(df['reviewVersion'],errors='coerce')
    # sort the lines by date
    df=df.sort_values(by='date')
    # sort the version that it is monotone increasing
    max=0
    for index, row in df.iterrows():
        if row['reviewVersion']>max:
            max=row['reviewVersion']
        else:
            df.loc[index:index,('reviewVersion')]=None
    sum=0
    n=0
    aver = []
    year = []
    # drop the lines which date = Nan, otherwise the year list will have some Nan element and can't plot normally
    df=df.dropna(subset=['date'])
    # get the first line's index for the 't1'
    for index, row in df.iterrows():
        initial_date_index = index
        break
    t1=df.loc[initial_date_index,'date']
    # calculate the average for each new month
    for index, row in df.iterrows():
        t = row['date']
        n=n+1
        sum=sum+row['compound']
        if (t.month-t1.month!=0)and(t.month!=None):
            # Each time a new month is traversed, the average is calculated and add to the list 'aver'
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
    # plot the version vertical lines
    if version_label_model==0:
        # the parkman versions is relatively less, so print the Parallel label
        for index, row in df.iterrows():
            if row['reviewVersion'] > max:
                max = row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1])) <= 1:
                    # considering the version is too much so that only plot the one decimal version
                    plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=8,
                             verticalalignment='bottom', rotation=40)
                    plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    print(row['reviewVersion'])
    if version_label_model==1:
        # the easypark versions is relatively more, so print the Interlaced label
        for index, row in df.iterrows():
            if row['reviewVersion']>max:
                max=row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1]))<=1:
                    # considering the version is too much so that only plot the one decimal version
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

plot_sentiment('polt_data/parkman.csv',1)
plot_sentiment('polt_data/easypark.csv',1)

