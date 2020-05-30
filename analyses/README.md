# The_One_with_All_the_Data


## combining_data.ipynb
This method combines a bunch of the CSV's together to create a nice CSV that tries to include as much information on the individual episodes as possible.  It includes the percent of the scenes that take place at big locations like: Joey's, Monica's and Ross's apartment as well as Central Perk.  It also does the same for percentage of lines said by each main character vs all lines in the episode (where a line is defined to be everything they said before a different person spoke).  It has which minor characters are in it, all of the credited actors, percentages of quotes, etc. So one may even think of this as the cleaning the dataset notebook more than analysis.

## K-Clustering Code (K-Means, K-Mode, K-Prototype).pynb
This Jupyter Notebook contains all the code for the K-clustering models in this project. The notebook begins by standardizing the variables used. Next, we use the numerical features to fit the K-Means model with three and four clusters. Since K-mean models use Euclidean distance to find the cluster centroids, it is not an appropriate model to use with categorical data.

As a second approach, we use the K-Modes clustering algorithm. The K-modes model defines clusters based on the number of matching categories between data points (Huang, 1997; Huang, 1998; Cao, 2009). For a brief explanation of how the K-Modes clustering algorithm works, please see the following short video on youtube: https://www.youtube.com/watch?v=b39_vipRkUo.

Lastly, we make use of the K-prototype clustering algorithm, which can take in both numerical and categorical variables (Huang, 1997; Huang, 1998; Cao, 2009). As a robustness check, we also fit the K-Prototype and K-Means clustering algorithms without any variable with sparse data. 

After inspection, we discover that all clustering algorithms employed on our data give similar clusterings. Thus, we focus our video on the K-Prototype clustering algorithm with sparse data. All clustering algorithm results can be found in the figures_and_results folder with the name K-Clusterin (Mean, Mode, Prototype).xlsx.



## NLP in multiple forms

### Topic Modeling via LDA
We tried to use LDA on all of Rachel's Line like in [this article](https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0).  We created a word cloud (after adding some extra stopping words).  After that we looked at the different "documents" where each was a string of all of the words that Rachel said in a particular episode and then ran it in our LDA model.  The version in this file was for 7 topics which we felt looked the best out of the others we had seen. It did not perform well, however, for a few reasons that make a lot of sense.  The first is when these scripts are made, the transcribers try to take into account stuttering and pauses like for example "wa-wa-what" or "ohhh...kay" these make sense when transcribing, but for LDA are hard to take into account such a large size of stopwords. The second big issues is the number of times the characters say eachother's name, after the stopwords are removed, Rachel says Ross's name the most and Monica says Chandler's.  However overall all the characters say eachothers name and nicknames so much a lot of what is being picked up is the names.
