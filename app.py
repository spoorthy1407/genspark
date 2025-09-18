from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-link', methods=['POST'])
def submit_link():
    product_url = request.form['product_url']
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(product_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').string
        return render_template('result.html', title=title)
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

if __name__ == '__main__':
    app.run(debug=True)
