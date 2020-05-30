# Episode info
This subfolder contains the info scraped from Wikipedia ('creators.csv') and the long summaries, also from Wikipedia.

Wikipedia was scraped for director, writers (screenplay and teleplay categories were collapsed as sometimes it was specified, and sometimes it was not), airdate (from which month was extracted to a new column), and number of viewers in the US in millions.

'episode_info.csv' contains the info scraped from IMDB. We used 'Rating' and 'short_summary' columns.

Both these .csv contain other information we scraped just in case.

'episode_info_merged.csv' is the resulting csv from merging the IMDB and Wikipedia information.

'number_quotes_in_episode.csv' contains the number of memorable quotes per episode in those episodes that contain memorable quotes. In all notebooks, whenever 'catchphrase' is used, it always stands for memorable quote.
