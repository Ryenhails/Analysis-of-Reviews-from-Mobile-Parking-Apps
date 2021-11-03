# Analysis-of-Reviews-from-Mobile-Parking-Apps
In this project, the students will collect Thousands of online reviews from Apple and Google Play stores from across Europe or at least Nordic area, to understand how users react to the two parking apps that run in the Nordic region - EasyPark and ParkMan. This project will provide insight into user behavior, sentiment toward parking apps and highlight the most important topics regarding users' requests, demands and preferences in terms of parking solutions or technology features.  


1.Write a script to download data for the two apps and save them in CSV files separately. Data collection involves getting user IDs, reviews, reviews’ ratings, reviews’ dates, and version history of the apps from Google play and Apple store. Additionally, you can collect other information if you wish. 

2.Ensure that all reviews are translated into English, clean the data, and process it. Concatenate the data from both stores but keep the two apps' data separate in two data-frames for further analysis. At the end you would have two datasets, one for EasyPark and another for ParkMan. 
The following tasks are to be performed for each app separately, except for 6, 7, 8, and 12 which are common to all:

3.Perform the sentiment analysis of the reviews and try to classify each review as either positive (1), negative (-1), or neutral (0). You can use sentiment Vader (https://github.com/cjhutto/vaderSentiment) and use the compound results to make the classification by specifying thresholds. Add the sentiment results to a distinct column in your datasets (data-frames).
-positive sentiment: compound score >= 0.05
-neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
-negative sentiment: compound score <= -0.05

4.Consider making two plots, one for ratings and another for sentiments over time. Use the date about new versions and new releases. Scatter these dates across each plot so you can observe the effect of the new version on the sentiment or rating.

5.We want to find the most discussed topics from users, and for that, perform LDA topic modeling and try to generate 10 topics. 

6.Train a machine learning model (random forest or another one) with positive and negative sentiment reviews. Try to use different n-gram representations such as n-gram (2,3) or (3,4). Then perform feature selection to identify the most important words or n-gram elements that impacted the classification for positive and negative classes. Try to specify the class for each word or element you retrieve.

7.The next task is about the use of technology acceptance models (TAM) to assess how people respond to technology adoption decisions. For instance, we try to measure the level of satisfaction, perceived ease of use, perceived usefulness, and attitudes toward the technology.

Try to learn more about TAM from this review paper [1]. We are interested in understanding how the indicators: perceived ease of use, perceived usefulness, satisfaction, attitude, and behavioral intentions change over time. You can check this paper [2] as well for more information about some of the TAM indicators.

7.2Examine the items of surveys and questionnaires found in the following related papers [3][4][5][6][7]; additionally, you may look for more relevant papers and surveys in Google Scholar. Then generate keyword lists for each indicator based on the elements of surveys and questionnaires. For instance: some keywords for satisfaction are {Satisfied, fulfill, gratify, meet, beneficial, content, happy, appeasement ……. etc.}.

7.3To augment the list of keywords, write a script that finds synonyms, hypernyms, and hyponyms for each word, by using WordNet database. Review the words manually and remove those which are not relevant.

7.4Perform necessary data processing for the list of keywords and reviews, for instance, Part of Speech tagging and lemmatization. Then classify each review and its data (rating, sentiment, and date) to a particular TAM indicator based on the common words. In the end, it is expected to have 5 data-frames, each one refers to data related to one TAM indicator.

7.5 Repeat task 4 for each indicator. 

7.6Calculate the Pearson correlation with a P value between different indicators and determine which are most strongly correlated. Highlight the correlations you find. Provide table to summarize your work. 



How To Run ? 

1 For Scrapping :
1.1 Libraries Needed 
-app_store_scraper 
-google_play_scraper 
-pandas
-numpy 
-json
-datetime
-dateutil
1.2 For Parkman:
-Just run normally, the code will scrap reviews from finland and denmark, in english, Finnish, and danish
-Just make sure there is an csv file in the same directory named parkman.csv with the correct header

1.3 For EasyPark:
-Because we scrapped from all over europe and we did not want to write long useless repetettive code, we kept changing in the parameters the
countries and the languages
-so for android part change the language from  en,fi,fr,es,no depending on the country but use english one time to not duplicate the data, and change the countries from fi,fr,es,no
-and for ios part change the country from fi,no,dk,se,fr,es,de
-Keep running again and again until getting the desired amount of data

2 For Translating:

2.1 Libraries needed

-datetime
-sys
-deep_translator 
-pandas

2.2 Running

-Running normally, just change the name of the file each time you want to translate, and make sure it is on the same directory of the python file


3 For First Impression Analysis  

3.1 Libraries needed 
 
-pandas
-dateutil 
-matplotlib
-nltk
-collections 
-string

3.2 For running

-Running is normal, just make sure there is two csv files named parkman_trans and easypark_trans that contain all the reviews in english
-it should be in the same folder


4 For Keyword expansion

4.1 Libraries needed

-nltk
-pandas

4.2 For running

-Running is normal, just make sure there is a csv file named indicators that we extracted from questionnaires in the same directory as the python file 

5 For plot task

-pandas
-matplotlib

6 For Random forest

-sklearn
-nltk
-numpy

7 For indicator classify

-pandas
-nltk
