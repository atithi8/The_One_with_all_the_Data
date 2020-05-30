# The_One_with_all_the_Data

Project name: The One with all the Data

Project members: Laura Fernandez Arroyo, Brooke Ogrodnik, Daniel Cisneros and Atithi Acharya

Project Inspired by: Erd&#337;s Bootcamp on Data Science that took place in May 2020

## Project Idea/Goals
- Modeling how different factors such as side characters, location of the scenes, director, or season may affect ratings of the Friends series episodes. 
- The goal is to try and understand just what makes a good episode and do things like recommend a specific episode of the show to watch.

Project slides in [Google Slides]( ) and the corresponding video can be viewed on [YouTube](  ) 

## A Few Caveats about our Project
- Other Friends Data Science projects exist, but looking at the relationship between the ratings and things like scene percentages appears to be novel and thus our project ignored the sentiment analysis and analysing who the "main" character was and other such things, a summary of some which can be found [here](https://towardsdatascience.com/the-one-with-all-the-friends-analysis-59dafcec19c5).  
- Friends has over 200 episodes which means that there is a whole lot of script material, however 200 is not a lot when one is trying to find relationships between episodes and thus many times did not do CV because we wanted to focus not on predicting (since the series is over) but on analysing what we do know about the episodes.

## In this repository
- figures_and_results contains excel files, pictures and graphs of our results
- app_code contains everything needed to run the two versions of our app that recommend an episode of Friends based on a few questions you answer.  However, by using the links in the README located in the folder, you can find the apps online.
- scraping contains the code used to scrape from the multiple different sources we were looking at
- data is all csvs and text files that were made throughout this project including the scripts of the tv show seperated by characters
- analysis is the code we used to draw conclusions on our data i.e. where things like clustering took place.
