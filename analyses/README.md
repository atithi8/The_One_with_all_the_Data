# The_One_with_All_the_Data


## combining_data.ipynb
This method combines a bunch of the CSV's together to create a nice CSV that tries to include as much information on the individual episodes as possible.  It includes the percent of the scenes that take place at big locations like: Joey's, Monica's and Ross's apartment as well as Central Perk.  It also does the same for percentage of lines said by each main character vs all lines in the episode (where a line is defined to be everything they said before a different person spoke).  It has which minor characters are in it, all of the credited actors, percentages of quotes, etc. So one may even think of this as the cleaning the dataset notebook more than analysis.

## K-Clustering Code (K-Means, K-Mode, K-Prototype).pynb
This Jupyter Notebook contains all the code for the K-clustering models in this project. The notebook begins by standardizing the variables used. Next, we use the numerical features to fit the K-Means model with three and four clusters. Since K-mean models use Euclidean distance to find the cluster centroids, it is not an appropriate model to use with categorical data.

As a second approach, we use the K-Modes clustering algorithm. The K-modes model defines clusters based on the number of matching categories between data points (Huang, 1997; Huang, 1998; Cao, 2009). For a brief explanation of how the K-Modes clustering algorithm works, please see the following short video on youtube: https://www.youtube.com/watch?v=b39_vipRkUo.

Lastly, we make use of the K-prototype clustering algorithm, which can take in both numerical and categorical variables (Huang, 1997; Huang, 1998; Cao, 2009). As a robustness check, we also fit the K-Prototype and K-Means clustering algorithms without any variable with sparse data. 

After inspection, we discover that all clustering algorithms employed on our data give similar clusterings. Thus, we focus our video on the K-Prototype clustering algorithm with sparse data. All clustering algorithm results can be found in the figures_and_results folder with the name K-Clusterin (Mean, Mode, Prototype).xlsx.
