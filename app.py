from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)

def is_phishing_link(url):
    parsed_url = urlparse(url)

    if "@" in parsed_url.netloc or "javascript:" in parsed_url.scheme:
        return True

    if parsed_url.netloc.replace(".", "").isdigit():
        return True

    if len(parsed_url.netloc.split(".")) > 5:
        return True

    if parsed_url.port and parsed_url.port not in [80, 443]:
        return True

    if "-" in parsed_url.netloc:
        return True

    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url_to_check = request.form['url']
        result = "is a phishing link" if is_phishing_link(url_to_check) else "is not a phishing link"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
