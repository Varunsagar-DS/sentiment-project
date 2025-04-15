import streamlit as st
from textblob import TextBlob
from pytube import YouTube
st.title("what you want to do")
tab_titles= ["Sentiment Analysis","Youtube Video Download"]
tabs=st.tabs(tab_titles)

with tabs[0]:
    st.header("**Sentiment Analysis**", divider='rainbow')

    st.write("")
    st.write("")

    st.sidebar.header("Contact Details")
    st.sidebar.write("Gmail - **varunkumarsagar74@gmail.com**")
    Lurl = "https://www.linkedin.com/in/varun-kumar-sagar-99b58b334/"
    Gurl = "https://github.com/Varunsagar-DS"
    st.sidebar.write("Linkedin - [Varun Kumar Sagar](%s)"%Lurl)
    st.sidebar.write("GitHub - [VarunSagar-DS](%s)"%Gurl)
    st.sidebar.header("About Sentiment Analysis project")
    st.sidebar.write('This is a machine learning project, in this project you have to give sentiments andit will reply with POSITIVE, NEGATIVE or NEUTRAL on basis of what kind of sentiment you gave.')


    text=st.text_input("**Input text**")
    btn=st.button("predict")

    if btn:
        blob=TextBlob(text)
        sen=blob.sentiment[0]
        if sen<0:
            st.error("Negetive Sentiment")
        elif sen>0:
            st.success("Positive Sentiment")
        elif sen==0:
            st.warning("Neutral Sentiment")

with tabs[1]:
    st.header("Youtube Video Downloader",divider="rainbow")

    st.sidebar.header("About Youtube Video Downloader project")
    st.sidebar.write('This is a Youtube Video Downloader project, in this project i have used pytube library which allows us to download videos from web. You have to enter the url and press enter and your video will be ready to download in the highest resolution of original video.''')



    link = st.text_input("**Enter URL**")

    if link:
        try:
            url = YouTube(link)

            video = url.streams.get_highest_resolution()

            st.write("Title of your video is :",url.title)

            btn=st.button("Download")

            if btn:
                video.download()
                st.success("Download Completed")
                
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("enter a url")
