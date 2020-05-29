#This part of the app is to choose whch type of episode you want to watch


import streamlit as st
import pandas as pd
import numpy as np

st.title('The One with the Recommendations')

st.write('This app is designed for helping you choose the particular episode of Friends that you are in the mood for. You have two ways to choose! One is via a supervised method and the other is the unsupervised method.')


option=st.selectbox('Which method would you like?',('Supervised','Unsupervised'))

if st.button('Tell me more about how this method works'):

	if option=='Supervised':
		st.write('insert summary here')

	if option=='Unsupervised':
		st.write('insert summary here') 


if st.button("Let's get started!"):
	if option=='Supervised':
		st.write('do something')
	if option=='Unsupervised':
		st.write('do something else')
