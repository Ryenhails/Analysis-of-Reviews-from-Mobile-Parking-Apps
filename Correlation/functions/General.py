import datetime
from os import listdir
import pandas
import seaborn as seaborn
import matplotlib.pyplot as plot


def readFile(path, column, size=10000):
    df = pandas.DataFrame(columns=['index', 'date'])
    df['index'] = range(1, size)
    date_range = pandas.date_range('1-1-2011', '1-1-2022', freq='m')
    df['date'] = pandas.Series(date_range.format())
    file_names = []

    for file in listdir(path):
        file_names.append(file)
        file_name = file.split('.')[0]
        csv_data = pandas.read_csv(path + file)
        csv_data['date'] = pandas.to_datetime(csv_data['date'])  # making sure dates are in uniform format
        csv_data = csv_data.sort_values(by="date")  # sorting by date
        csv_data = csv_data[['date', column]]
        csv_data = monthlyMean(csv_data)
        csv_data.index = pandas.Series(csv_data.index.format())
        csv_data['date'] = csv_data.index

        csv_data = csv_data.dropna()  # dropping null dates or column value
        csv_data[file_name] = csv_data[column]
        # csv_data['index'] = range(1, len(csv_data) + 1)  # adding an index column
        df = pandas.merge(df, csv_data[['date', file_name]], on='date', how='left')
        df = df.dropna()

    df.to_csv('./data/results/test.csv')

    return df


def correlationMatrix(matrix):

    correlation_matrix = matrix.corr()

    seaborn.heatmap(correlation_matrix, annot=True)

    plot.show()

def monthlyMean(column):

    column.index = column['date']

    return column.groupby(pandas.Grouper(freq='M')).mean()


