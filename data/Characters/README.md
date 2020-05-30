# Character Information

As mentioned in the scraping README, [here](https://www.kaggle.com/ryanstonebraker/friends-transcript) and [here](https://www.kaggle.com/ryanstonebraker/friends-transcript/version/1) exist databases of these scripts.  However, they do not take into accound scene location or asides mentioned in the script like (to joey) which we thing really adds something to the data analysis that we can now do. HTML scraping is never an exact science and thus these files are not perfect.  There are random Commercial Breaks floating around that should taken into account and at times some names might be misspelled and are thus repeated in the all_char file.  As with any data set, proceede with caution.  Hopefully, however, you find it more useful than scraping for hours yourself.


## Main Characters and other characters

Each of the 6 characters, and the All csv contain the following: [season, episode, scene, quote_index, line, extra]
Most of these are self explainitory but quote_index is the order that particular line was said in the screne so if you wanted to combine all the datasets into the scripts, you have all the puzzel pieces.  The extra portion is any assides mentioned during that line like [to joey] or [monica leaves the room]  

The other character lines are recorded in minors.csv and have the same information except an extra column for their name.

## all_char and scenes

all_char is a copy of every character's name that is located in the above dataframes along with True if they are one of the 6 and False else

scenes gives you [season,	episode, scene,	location,	extra_scene_info] the scene column is just numbering the scenes that took place in that episode, location is where they are at and the extra_scene_info is the attempt to parse information about the scene from the location itself.  Note that when the scenes were difficult to parse for this, the code just threw everything into scene location. 


## A Few examples of fun searches you could do with these csv's besides the ones we included in here

### You can print all instances of monica saying, "I know!" in the script

counter=0
pos=[]
for line in monica.line:
    if str(line).lower().find("i know!")>-1 :
        pos.append(counter)
    counter=counter+1
    
 ### Janice's, "Oh my God" gets a little more difficult though
counter=0
janice=minors.loc[minors.character=='janice']
pos=[]
for line in janice.line:
    if str(line).lower().find("my god")>-1 or line.lower().find("gawd")>-1 or line.lower().find("gaa")>-1 :
        pos.append(counter)
    counter=counter+1

print(len(janice.iloc[pos]))
janice.iloc[pos]

print(len(monica.iloc[pos]))
monica.iloc[pos]
