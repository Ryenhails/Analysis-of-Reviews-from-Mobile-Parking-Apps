import pandas as pd
import matplotlib.pyplot as plt
def plot_rating(csv_filename,version_label_model):
    # csv_filename=filename
    # version_label_model=0,1(0 means Parallel label and 1 means Interlaced label)
    df=pd.read_csv(csv_filename,sep = ';')
    df=df.sort_values(by='date')
    # sort the lines by date
    df['date']=pd.to_datetime(df['date'],format='%Y-%m-%d',errors='coerce')
    df['reviewVersion']=pd.to_numeric(df['reviewVersion'],errors='coerce')
    df['rating']=pd.to_numeric(df['rating'],errors='coerce')
    # convert object(date,version,rating) to datatime and numeric
    sum=0
    n=0
    aver=[]
    year=[]
    df=df.dropna(subset=['date'])
    # drop the lines which date = Nan, otherwise the year list will have some Nan element and can't plot normally
    for index, row in df.iterrows():
        initial_date_index=index
        break
    # get the first line's index for the 't1'
    t1=df.loc[initial_date_index,'date']
    # calculate the average for each new month
    for index, row in df.iterrows():
        t = row['date']
        n=n+1
        sum=sum+row['rating']
        if (t.month-t1.month!=0)and(t.month!=None):
            # Each time a new month is traversed, the average is calculated and add to the list 'aver'
            a = sum / n
            print(a)
            aver.append(a)
            year.append(row['date'])
            n = 1
            t1 = t
            sum = row['rating']
            print(row['date'])
    plt.plot(year, aver)
    max=0
    k=0
    # sort the version that it is monotone increasing
    for index, row in df.iterrows():
        if row['reviewVersion']>max:
            max=row['reviewVersion']
        else:
            df.loc[index:index,('reviewVersion')]=None
            # plot the version vertical lines
            max = 0
    if version_label_model == 0:
        # the parkman versions is relatively less, so print the Parallel label
        for index, row in df.iterrows():
            if row['reviewVersion'] > max:
                max = row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1])) <= 1:
                    # considering the version is too much so that only plot the one decimal version
                    plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=8,
                             verticalalignment='bottom', rotation=45)
                    plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
    if version_label_model == 1:
        # the easypark versions is relatively more, so print the Interlaced label
        for index, row in df.iterrows():
            if row['reviewVersion'] > max:
                max = row['reviewVersion']
                if (len(str(row['reviewVersion']).split('.')[1])) <= 1:
                    # considering the version is too much so that only plot the one decimal version
                    k = k + 1
                    if (k % 2 == 0):
                        plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=8,
                                 verticalalignment='bottom', rotation=38)
                        plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    else:
                        plt.text(row['date'], plt.axis()[3], 'Version:' + str(row['reviewVersion']), fontsize=8,
                                 verticalalignment='top', rotation=-38)
                        plt.axvline(row['date'], linestyle="dashed", color="#F5DEB3")
                    print(row['reviewVersion'])
    plt.show()

plot_rating('polt_data/parkman.csv',1)
plot_rating('polt_data/easypark.csv',1)


