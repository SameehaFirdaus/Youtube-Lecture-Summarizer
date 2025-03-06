# YouTube Lecture Summarizer

A Python application that summarizes YouTube lectures by extracting transcripts and generating concise summaries using AI.

## Features

- Extracts video metadata (title, channel).
- Fetches transcripts from YouTube videos.
- Summarizes transcripts using OpenAI's GPT model.
- User-friendly interface built with Streamlit.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SameehaFirdaus/youtube-lecture-summarizer.git
   cd youtube-lecture-summarizer
   
Install the required packages:

bash
Run
Copy code
pip install -r requirements.txt
Set up your OpenAI API key in an environment variable:

bash
Run
Copy code
export OPENAI_API_KEY='your-api-key-here'
Run the application:

bash
Run
Copy code
streamlit run app.py
