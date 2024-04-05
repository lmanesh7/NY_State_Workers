"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import os

df = pd.read_excel(r'AFB Data Wishlist-AC Data by Lost Time Group.xlsx')
arr = os.listdir()
unique_values = set(df[r'NAICS - 2 Digit Description (Industry)'])


st.write(df)
option = st.selectbox(
    'Select the Industry to view',
    unique_values)
try:   
    ff = 'AFB '+option+'.xlsx'
    df1 = pd.read_excel(ff)
    st.title(option)
    st.write(df1)
except:
    st.write("Some ERROR occured!!")

for f in arr:
    
    if f.find(ff)!=-1:
        st.write(f) 

