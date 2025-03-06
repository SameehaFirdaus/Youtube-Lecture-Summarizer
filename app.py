import streamlit as st
from scrape_youtube import extract_video_id, extract_metadata, get_transcript
from summarize_text import summarize_text

def main():
    st.title("YouTube Lecture Summarizer")
    url = st.text_input("Enter YouTube URL:")
    if st.button("Summarize"):
        try:
            video_id = extract_video_id(url)
            title, channel = extract_metadata(url)
            transcript = get_transcript(video_id)
            summary = summarize_text(transcript)
            
            st.subheader("Title:")
            st.write(title)
            st.subheader("Channel:")
            st.write(channel)
            st.subheader("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
