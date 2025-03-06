import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

def extract_metadata(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.find("title").text
    channel = soup.find("link", itemprop="name")['content']
    return title, channel

def get_transcript(video_id):
    transcript_raw = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_full = ' '.join([i['text'] for i in transcript_raw])
    return transcript_full
