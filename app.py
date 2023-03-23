from flask import Flask, render_template, request 
from extractor import extract_yturl
from settings import FEATURES, FAQS


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", features=FEATURES, faqs=FAQS)


@app.route("/download", methods=["POST"])
def download():
    video_url = request.form["video_url"]
    if "youtu.be" in video_url:
        video_data = extract_yturl(video_url)
        title = video_data["title"]
        thumbnail = video_data["thumbnail"]
        formats = video_data["formats"]
        Audio = video_data["Audio"]
        return render_template("YT_download.html",
                            title=title,
                            thumbnail=thumbnail,
                            formats=formats,
                            Audio = Audio,
                            features=FEATURES,
                            faqs=FAQS)
        
if __name__ == "__main__":
    app.run(debug=True)
