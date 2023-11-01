from flask import Flask,render_template, request
import requests, datetime

app = Flask(__name__)

@app.route("/")
def show_home():
    return render_template('index.html')

@app.route("/search", methods=['POST', 'GET'])
def home():
    current_date = datetime.datetime.now().date()
    date = current_date - datetime.timedelta(days=2)
    print(date)
    url = "https://newsapi.org/v2/everything"
    param = {
        'q':request.form.get('search'),
        'from':date,
        'sortBy':'popularity',
        'apiKey':'319f1986331947aa99f4dcb9ad51befd'
    }
    response = requests.get(url, params=param)
    data = response.json()
    articles = data['articles']

    table = f"<table border=1>"

    for article in articles:
        headline = article['description']
        url = article['url']
        table += f"<tr><td>{headline}</td><td><a href={url}>Link</a></td></tr>"
    table += '</table>'
    return table

    if __name__=='__main__':
        app.run(debug=True)