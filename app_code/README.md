# The One with the Recommendations

Hi and welcome to our app! The purpose is to take a few things that matter to you: Main characters, side characters, locations, keyword, etc and output a recommendation of 5 episodes of Friends!  There are two versions, one that uses a constrained technique and the other that uses an unsupervised one.  You can go directly to playing with these apps or you can first learn a bit more about how each one works below.

## Play with the apps
- [Constrained](https://afternoon-inlet-95580.herokuapp.com/) 
- Unsupervised (follow the download directions below)

## Inspiration for the app
When analysisng the scripts we found that a higher rating (on imdb) in episode usually means that Ross and Rachel are both talking more than they usually do and that the episode a very high percentage of scenes at Monica's Apartment.  This was the inspiration for the app. Companies like Netflix give us recommendations about what tv series or movie we might like, but they don't recommend a specific tv show.  If you know you want to watch Friends, but aren't sure if you feel like begining the long process of binging it, then you probably just want a couple of episodes that are quailty (not that the entire series isn't quality).  

## About Constrained
The constrained version takes in a max of one character, one location, one side character and one keyword.

### How the algorithm works:
- Takes the character (if one is chosen) and searches the database for the top 5 episodes in which the percentage of lines that character speaks vs all lines in the episode is highest
- Takes the location (if one is chosen) and searches the database for the top 5 episodes in which the percentage of scenes located there vs all scenes in the episodes is highest
- Takes the side character (if one is chosen) and searches for the top 5 episodes in which that character is present.  Note that one of the reasons we picked these characters is because they have all appeared in at least 5 episodes, some like Gunther appeared in much more.
- Takes the keyword and searches the wikipedia summaries for the keyword again taking the top 5 episodes 
- Combine all of these episodes into a list, and sort them by those that appeared most to least and breaking ties via their ratings.  
- Return the first 5 in the list.
- If there was too much over lap and 5 cannot be returned fill in the end with just top rated episodes that were not yet reccomended.

### A caveat about this method
The algorithm is a little wordy to explain because we had to make some tough choices about how to choose which inputs mattered the most or a systematic way of combining them for what we thought was a fitting algorithm.  One notices that when Monica's Apartment is chosen via this method, and no extra keyword is mentioned, you will usually get the same reccomendations.  This is due to the fact that such high ranked episodes took place at her apartment and without a keyword they end up getting to the top of the list.  So a keyword is recommended if you want a good variety in your answers while still choosing Monica's Apartment.  Another option is to compare what you get from this version to the unsupervised version and taking both lists into account decide the episode you are in the mood for.




## About Unsupervised

















## Directions to run the apps locally

- Download the files
- Make sure that you have streamlit installed 
- Open the terminal and locate the folder you downloaded
- Streamlit run app_hardcode.py inside said folder for the constrained app
- Streamlit run app_unsupervised.py inside said folder for the unsupervised app



