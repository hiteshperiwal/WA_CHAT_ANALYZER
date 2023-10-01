import streamlit as st
import preprocessor
import pandas as pd
st.sidebar.title("Whatsapp Chat Analzer")

#streamlit run app.py
#streamlit documentation upload ...copy the lines
    
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #stream to string file convert
    data=bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    #st.text(data)
    st.dataframe(df)
    
    #fetch unique users
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")  #position and then insert
    st.sidebar.selectbox("Show analysis wrt",user_list)
    
    if(st.sidebar.button("Show Analysis"):
        col1,col2,col3,col4=st.beta_columns(4)
    
    


    
