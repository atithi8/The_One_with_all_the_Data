# this is an app whose purpose is to reccomend a show based on some input by
# the user.

import streamlit as st
import pandas as pd
import sklearn
import numpy as np
import nltk 

#nltk.download('stopwords')

#############################################################################
#dataset=pd.read_csv('for_app_hardcode.csv')
wiki_sum=pd.read_csv("data/summaries_Wiki.csv")
dataset_ati=pd.read_csv("data/with_rows_removed_addedrows.csv")
#sum_table=dataset["1line_sum"]
sum_table=wiki_sum["summary"]

def run_sim_code(keyword):
    sentences = []
    for s in sum_table:
        sentences.append(s)

    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

    word_embeddings = {}

    #f = open('glove.6B.100d.txt', encoding='utf-8')

    f = open("data/glove.6B.100d.txt", encoding='utf-8')

    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()

    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')


    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new

    clean_sentences = [s.lower() for s in clean_sentences]
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            #print('I am here')
            #Need to change 100 if we change here use diff text
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)

    from sklearn.metrics.pairwise import cosine_similarity


    sentence_query=[keyword]
    clean_sentence_query = pd.Series(sentence_query).str.replace("[^a-zA-Z]", " ")

    clean_sentence_query = [s.lower() for s in clean_sentence_query]
    clean_sentence_query = [remove_stopwords(r.split()) for r in clean_sentence_query]


    sentence_vector_query = []

    for i in clean_sentence_query:
        if len(i) != 0:
            #print('I am here')
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vector_query.append(v)


    t_len=len(sentences)

    sim_mat1 = np.zeros([1, t_len])

    for i in range(1):
        for j in range(t_len):
            if i != j:
                sim_mat1[i][j] = cosine_similarity(sentence_vector_query,
                                                  sentence_vectors[j].reshape(1,100))[0,0]

    #n=t_len            
    n=5

    sort_l=np.array(list(sim_mat1.reshape(sim_mat1.shape[1]))).argsort()[::-1][:n]

    final_index=[]
    final_index=[sort_l[0],sort_l[1],sort_l[2],sort_l[3],sort_l[4] ]

    return final_index


# sum_table[sort_l[0]]
# sum_table[sort_l[1]]
# sum_table[sort_l[2]]
# sum_table[sort_l[3]]
# sum_table[sort_l[4]]

#############################################################################

st.title('The One with the Recommendations')

st.write('Tell us about what you are looking for in an episode and we will reccomend the 5 highest rated episodes that best match your preferences')

ready=True

st.header('Choose 2-3 characters')

collect_entry=''
#start with none of them chosen
rachel, monica, phoebe, ross, joey, chandler =['']*6
r, m, p, ro, j, c, pref_char=[0]*7
if st.checkbox('Rachel'):
    rachel='rachel'
    r=1
    collect_entry+='rachel'

if st.checkbox('Monica'):
    monica='monica'
    m=1
    collect_entry+=' monica'
if st.checkbox('Ross'):
    ross='ross'
    ro=1
    collect_entry+=' ross'

if st.checkbox('Joey'):
    joey='joey'
    j=1
    collect_entry+=' joey'

if st.checkbox('Chandler'):
    chandler='chandler'
    c=1
    collect_entry+=' chandler'

if st.checkbox('Phoebe'):
    phoebe='phoebe'
    p=1
    collect_entry+=' phoebe'

if st.checkbox('No preference for main character') :
    pref_char=1

if (p+r+m+c+ro+j!=2 and r+p+m+c+j+ro!=3) and pref_char==0:
    st.warning('Please choose between 2 or 3')
    ready=False
elif pref_char==1 and p+r+m+c+ro+j!=0:
    st.warning('Either you care or you don\'t!')
    ready=False

st.header('Choose a side character')
gunther, janice, richard, heckles, carol, frank, estelle, ursula, pref_side=[0]*9

if st.checkbox('Gunther'):
    gunther=1
    collect_entry+=' gunther'

if st.checkbox('Janice'):
    janice=1
    collect_entry+=' rachel'
if st.checkbox('Richard'):
    richard=1
    collect_entry+=' richard'

if st.checkbox('Mr Heckles'):
    heckles=1
    collect_entry+=' Mr Heckles'

if st.checkbox('Carol'):
    carol=1
    collect_entry+=' carol'

if st.checkbox('Frank'):
    frank=1
    collect_entry+=' frank'

if st.checkbox('Estelle'):
    estelle=1
    collect_entry+=' estelle'

if st.checkbox('Ursula'):
    ursula=1
    collect_entry+=' ursula'

if st.checkbox('No preference for side character'):
    pref_side=1


if gunther+janice+richard+heckles+carol+frank+estelle+ursula!=1 and pref_side!=1:
    st.warning('Please choose exactly 1')
    ready=False
elif pref_side==1 and gunther+janice+richard+heckles+carol+frank+estelle+ursula>0:
    st.warning('Either you care or you don\'t!')
    ready=False

# st.header('Choose a location')

# central_perk, monicas, joeys, rosses, pref_loc=[0]*5
# ## [0]*5

# if st.checkbox('Central Perk'):
#   central_perk=1
# if st.checkbox('Monica\'s Apartment'):
#   monicas=1
# if st.checkbox('Joey\'s Apartment'):
#   joeys=1
# if st.checkbox('Ross\' Apartment'):
#   rosses=1
# if st.checkbox('No preference for location'):
#   pref_loc=1

# if central_perk+monicas+joeys+rosses+pref_loc!=1:
#   st.warning('Please choose exactly 1')
#   ready=False

    

#submit=st.button('Recommend')
    
st.header('Keyword')
st.write('please seperate each word with a comma')
keyword= st.text_input('search for')

spoil=st.checkbox('No spoilers! Hide the summaries of the recommendations.')


submit=st.button('Submit')



if submit and ready:
    
    collect_entry+=' '+keyword
    #st.write('now run the code here')
    keyword=keyword+' '+ross+' '+rachel+' '+phoebe+' '+joey+' '+monica+' '+chandler
    #st.write('keyword before',keyword)
    st.write('Your entries:', collect_entry)
    
    final_index=run_sim_code(collect_entry)
    #st.write('entry after',collect_entry)
    
    st.write(dataset_ati.iloc[final_index][['season','episode','title']])
    if not spoil:
        for i in final_index:
            st.write(dataset_ati.iloc[i].title+': '+ wiki_sum.iloc[i].summary)

elif submit and not ready:
    st.error('Please fix the warnings and then resubmit')

