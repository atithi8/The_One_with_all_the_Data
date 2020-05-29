# The_One_with_All_the_Data

## Where we scraped files from
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_Friends_episodes) for the directors, teleplay, story by, month of episode, number of viewers
- [Wikipedia](https://en.wikipedia.org/wiki/Friends_(season_1)) for the summaries of the episodes
- [Imdb](https://www.imdb.com/title/tt0108778/) for the title, short summary, list of actors, ratings, and number of ratings
- [Github code](https://fangj.github.io/friends/) for the scripts, though we downloaded the files, added the occasional missing closing parenthesis, closing bracket, and replaced 2:00 to 2pm to help with the scraping.
- [Github code](https://brookeogrodnik.github.io/scripts/0101.html) The edited version is currently on Brooke's github page


## About the Friends Script Scrapings
The github that we origonally got the scripts from is a wonderful resource except that a wide range of people contributed to it, each transcribing in a slightly different way.  Given that we were HTML scraping using Beautiful Soup, this made the task difficult. Some things that we had to deal with was,
- A few episodes where MNCA was written instead of Monica and RACH instead of Rachel, etc.  
- Cases of: 'Monica: monicas lines', 'Monica:' 'monicas lines' , and  'Monica' ': monicas lines', 'Monica (to joey)' ': monicas lines' 
- \[Scene , \(scene, \[Flashback Scene, Scene 
- 'Transcribed by: ',  'Transcribed', 'Transcriber' 
- Wrong or mispelled title names 
- missing closing parenthesis
- All, Everyone, Everybody used interchangably 
- and more

One way we attacked this was by downloading the scripts and reuploading them on another github where we had the ability to edit the parts that would break the code. Other than that, the fix was a whole lot of extra conditions that we searched through when parsing the script and taking out things like recaps.  There is no way that we got all of they typos/ weird formatting into account, however any problems should be far and few between and should thus not have a noticable effect on our analysis. 

One last note is if one looks at the other Friends Data Science projects in the world, it appears that everyone has used this resource for their codes.  There exist Kaggle Databases with the scripts [Here](https://www.kaggle.com/ryanstonebraker/friends-transcript) and [Here](https://www.kaggle.com/ryanstonebraker/friends-transcript/version/1) but they did not include things like scene locations which we believed to be important and some skipped some the of the more problem episodes all together.  


### The output
The scripts were outputed into csv's for each of the 6 main characters, a csv for scenes, a csv for minor characters, a csv with lines for 'All:' and one that is a master list of characters.  More on this can be seen in the data readme.
