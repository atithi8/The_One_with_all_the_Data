# this is an app whose purpose is to reccomend a show based on some input by
# the user.


import streamlit as st
import pandas as pd
import numpy as np



st.title('The One with the Recommendations')

st.write('Tell us about what you are looking for in an episode and we will reccomend the 5 highest rated episodes that best match your preferences')

ready=True

st.header('Choose 2-3 characters')

#start with none of them chosen
rachel, monica, phoebe, ross, joey, chandler =['']*6
r, m, p, ro, j, c, pref_char=[0]*7
if st.checkbox('Rachel'):
	rachel='rachel'
	r=1

if st.checkbox('Monica'):
	monica='monica'
	m=1

if st.checkbox('Ross'):
	ross='ross'
	ro=1

if st.checkbox('Joey'):
	joey='joey'
	j=1

if st.checkbox('Chandler'):
	chandler='chandler'
	c=1

if st.checkbox('Phoebe'):
	phoebe='phoebe'
	p=1

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
if st.checkbox('Janice'):
	janice=1
if st.checkbox('Richard'):
	richard=1
if st.checkbox('Mr Heckles'):
	heckles=1
if st.checkbox('Carol'):
	carol=1
if st.checkbox('Frank'):
	frank=1
if st.checkbox('Estelle'):
	estelle=1
if st.checkbox('Ursula'):
	ursula=1
if st.checkbox('No preference for side character'):
	pref_side=1

if gunther+janice+richard+heckles+carol+frank+estelle+ursula!=1 and pref_side!=1:
	st.warning('Please choose exactly 1')
	ready=False
elif pref_side==1 and gunther+janice+richard+heckles+carol+frank+estelle+ursula>0:
	st.warning('Either you care or you don\'t!')
	ready=False

st.header('Choose a location')
central_perk, monicas, joeys, rosses, pref_loc=[0]*5

if st.checkbox('Central Perk'):
	central_perk=1
if st.checkbox('Monica\'s Apartment'):
	monicas=1
if st.checkbox('Joey\'s Apartment'):
	joeys=1
if st.checkbox('Ross\' Apartment'):
	rosses=1
if st.checkbox('No preference for location'):
	pref_loc=1

if central_perk+monicas+joeys+rosses+pref_loc!=1:
	st.warning('Please choose exactly 1')
	ready=False

st.header('Keyword')
st.write('please seperate each word with a comma')
keyword= st.text_input('search for')

submit=st.button('Submit')

if submit and ready:
	#do things
	st.write('now run the code here')
	keyword=keyword+' '+ross+' '+ rachel+ ' '+phoebe+' '+joey+' '+monica+' '+chandler
	st.write(keyword)

elif submit and not ready:
	st.error('Please fix the warnings and then resubmit')

