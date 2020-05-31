# The One with the Recommendations

Hi and welcome to our app! The purpose is to take a few things that matter to you: Main characters, side characters, locations, keyword, etc and output a recommendation of 5 episodes of Friends!  There are two versions, one that uses a constrained technique and the other that uses an unsupervised one.  You can go directly to playing with these apps or you can first learn a bit more about how each one works below.

## Play with the apps
- [Constrained](https://afternoon-inlet-95580.herokuapp.com/) 
- Unsupervised(follow the download directions below)

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
Input: The unsupervised version takes in multiple characters, one side character and can take many keywords

### How the algorithm works:
- Collect summaries obtained from Wikipedia for each of the episodes and then pre-process it which includes cleaning i.e. remove extra spaces etc. 
- We also remove stopwords such as "the", "a", "I", etc importing from the NLTK library.
- After the preprocessing, we tokenize or break down the entire text corpus into tokens (words). Further, we use Word Embeddings such as glove or word2vec that was built to build vector representations of each summary
- We then also convert our input phrase which contains all the inputs given by the user 
- Compute scores using a cosine similarity metric between the vector representation of the input phrase and that of the corresponding context vectors of episode summaries. 


### Caveat of this method
There is a lack of a way to validate the predictions that the algorithm makes since we are limited to a completely unsupervised setting and also recommendations can't be put into correct or incorrect labels. However qualitatively it could be judged how good the recommendation by the app performs.


### Scope of improvement
We can do a similarity search between the input phrase and the entire text corpus of each episode which will make the predictions better and will also include more sophisticated entry into the keyword input. Also, we can create a context vector by actually trying to learn a summary using higher levels of a network-like similarity searches i.e. page ranking system from the entire text corpus of an episode. This can help us generalize further into other tv shows.



## Directions to run the apps locally
(For the unsupervised version: Also download an extra file from the following [link] (https://drive.google.com/file/d/1yzXSCxyfqut0KvPiVYQ2q6B2KC3ZDxvJ/view?usp=sharing) )

- Download the files 
- Make sure that you have streamlit installed 
- Open the terminal and locate the folder you downloaded
- Streamlit run app_hardcode.py inside said folder for the constrained app
- Streamlit run app_unsupervised.py inside said folder for the unsupervised app




