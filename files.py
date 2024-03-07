import streamlit as st
import pandas as pd

st.subheader('Uploading the CSV File')
df = st.file_uploader("Upload the CSV file : ", type = ['csv','xlsx'])
if df is not None:
    st.dataframe(df)


st.subheader('Loading the CSV File')
df = pd.read_csv('Products.csv')
if df is not None:
    st.table(df.head())


st.subheader('Uploading the Image File')
img = st.file_uploader("Upload the Image file : ", type = ['png','jpeg'])
if img is not None:
    st.image(img)


st.subheader('Uploading the Videos file')
video_file = st.file_uploader("Upload the Video file : ", type = ['mkv','mp4'])
if video_file is not None:
    st.video(video_file)


st.subheader('Loading the audio file')
audio_file = st.file_uploader("Upload the Audio file : ", type = ['wav','mp3'])
if audio_file is not None:
    st.audio(audio_file)





