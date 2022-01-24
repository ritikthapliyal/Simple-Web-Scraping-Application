from flask import Flask,render_template
import my_scraper

app = Flask(__name__)
data = my_scraper.news

@app.route("/")
def news_app():
    return render_template('index.html',data = data)


if __name__ == "__main__":
    app.run(debug=True)