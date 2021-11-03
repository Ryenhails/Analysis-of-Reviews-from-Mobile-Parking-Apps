# Analysis-of-Reviews-from-Mobile-Parking-Apps

#There are detailed descriptions of each task and the corresponding code/data folders#

#All tasks have been done#

1.Write a script to download data for the two apps and save them in CSV files separately. Data collection involves getting user IDs, reviews, reviews’ ratings, reviews’ dates, and version history of the apps from Google play and Apple store. Additionally, you can collect other information if you wish. 

For this task:
/Scrapping

2.Ensure that all reviews are translated into English, clean the data, and process it. Concatenate the data from both stores but keep the two apps' data separate in two data-frames for further analysis. At the end you would have two datasets, one for EasyPark and another for ParkMan. 
The following tasks are to be performed for each app separately, except for 6, 7, 8, and 12 which are common to all:

For this task:
/Translating

3.Perform the sentiment analysis of the reviews and try to classify each review as either positive (1), negative (-1), or neutral (0). You can use sentiment Vader (https://github.com/cjhutto/vaderSentiment) and use the compound results to make the classification by specifying thresholds. Add the sentiment results to a distinct column in your datasets (data-frames).
-positive sentiment: compound score >= 0.05
-neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
-negative sentiment: compound score <= -0.05

For this task:
/SentimentAnalysis

4.Consider making two plots, one for ratings and another for sentiments over time. Use the date about new versions and new releases. Scatter these dates across each plot so you can observe the effect of the new version on the sentiment or rating.

For this task:
/plot_data

5.We want to find the most discussed topics from users, and for that, perform LDA topic modeling and try to generate 10 topics. 

For this task:
/TopicModeling

6.Train a machine learning model (random forest or another one) with positive and negative sentiment reviews. Try to use different n-gram representations such as n-gram (2,3) or (3,4). Then perform feature selection to identify the most important words or n-gram elements that impacted the classification for positive and negative classes. Try to specify the class for each word or element you retrieve.

For this task:
/randomforest_data

7.The next task is about the use of technology acceptance models (TAM) to assess how people respond to technology adoption decisions. For instance, we try to measure the level of satisfaction, perceived ease of use, perceived usefulness, and attitudes toward the technology.
Try to learn more about TAM from this review paper [1]. We are interested in understanding how the indicators: perceived ease of use, perceived usefulness, satisfaction, attitude, and behavioral intentions change over time. You can check this paper [2] as well for more information about some of the TAM indicators.

7.2Examine the items of surveys and questionnaires found in the following related papers [3][4][5][6][7]; additionally, you may look for more relevant papers and surveys in Google Scholar. Then generate keyword lists for each indicator based on the elements of surveys and questionnaires. For instance: some keywords for satisfaction are {Satisfied, fulfill, gratify, meet, beneficial, content, happy, appeasement ……. etc.}.

7.3To augment the list of keywords, write a script that finds synonyms, hypernyms, and hyponyms for each word, by using WordNet database. Review the words manually and remove those which are not relevant.

For this task:
/TAMKeywordExpansion

7.4Perform necessary data processing for the list of keywords and reviews, for instance, Part of Speech tagging and lemmatization. Then classify each review and its data (rating, sentiment, and date) to a particular TAM indicator based on the common words. In the end, it is expected to have 5 data-frames, each one refers to data related to one TAM indicator.

For this task:
/indicators

7.5 Repeat task 4 for each indicator. 

For this task:
/plot_indicators_data

7.6Calculate the Pearson correlation with a P value between different indicators and determine which are most strongly correlated. Highlight the correlations you find. Provide table to summarize your work. 

For this task:
/Correlation



