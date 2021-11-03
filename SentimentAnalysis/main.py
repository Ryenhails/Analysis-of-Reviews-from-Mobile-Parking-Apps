from classes.vader.SentimentIntensityAnalyzer import SentimentIntensityAnalyzer
from constants.general import DATA_DIR
import pandas

if __name__ == '__main__':

    df = pandas.read_csv(DATA_DIR+"parkman_trans.csv", sep=";", error_bad_lines=False)

    analyzer = SentimentIntensityAnalyzer()
    #print(df.iloc[614]["content"])
    print("-----------------------START-----------------------------")

    for i in range(0, len(df)):
        vs = analyzer.polarity_scores(df.iloc[i]["content"])
        sentm = "unknown"

        if vs['compound'] >= 0.5:
            sentm = "positive"
        elif -0.5 <= vs['compound'] < 0.5:
            sentm = "neutral"
        elif vs['compound'] < -0.5:
            sentm = "negative"

        print("{:-<65} {}".format(df.iloc[i]["content"], str(vs['compound'])))
        with open(DATA_DIR+"parkman_sentiment.csv", 'a') as fd:
            user = df.iloc[i]["userName"]
            text = df.iloc[i]["content"]
            rating = df.iloc[i]["rating"]
            date = df.iloc[i]["date"]
            version = df.iloc[i]["reviewVersion"]
            if i == 0:
                fd.write("ind;userName;content;rating;date;reviewVersion;compound;sentiment \n") # place header at the top of the file
            fd.write(str(i) + ";" + str(user) + ";" + str(text) + ";" + str(rating) + ";" + str(date) + ";" + str(
                version) + ";" + str(vs['compound']) + ";" + sentm + "\n")

    print("----------------------THE END------------------------------")
