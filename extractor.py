import os
import json
import requests
from bs4 import BeautifulSoup
from pytube import Playlist




#Youtube start

def extract(data_form):
    url = data_form["url"]
    format_name = data_form["format_note"]
    return{
        "url" : url,
        "name" : format_name
    }



def extract_yturl(url):
    command = f'yt-dlp "{url}" -j'
    output = os.popen(command).read()
    video_data = json.loads(output)
    title = video_data["title"]
    formats = video_data["formats"]
    thumbnail = video_data["thumbnail"]
    form = []
    for i in formats:
            video = i["vcodec"]
            audio = i["acodec"]
            channel = i["resolution"]
            formats = i["format"]
            formats_id = i["format_id"]
            if((video =="avc1.64001F") and (audio=="mp4a.40.2")):
                form.append(extract(i))
            if((video =="avc1.42001E") and (audio=="mp4a.40.2")):
                form.append(extract(i))
            if((formats_id == "139") and ((audio == "mp4a.40.5") or (audio == "opus") or (audio == "mp4a.40.2"))):
                Audio_url = i["url"]
                Audio = f'{Audio_url}&title={title.replace(" ","")}'
    return {
        "title": title,
        "formats": form,
        "thumbnail": thumbnail,
        "Audio" : Audio
        }

#Youtube end







