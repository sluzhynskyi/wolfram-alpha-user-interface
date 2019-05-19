from flask import Flask, render_template, request, jsonify
# Using for encoding latex equation to url.
import urllib.parse
# Using for check if request that user entered is valid?
from modules.wolfram_valid import valid
# Using ADT
from modules.my_str import MyStr

app = Flask(__name__, static_url_path="/static", )


@app.route("/")
def index():
    """
    Home page,which = index.html
    """
    return render_template("index.html")


@app.route("/redirect_to_wolfram", methods=["POST"])
def redirect_to_wolfram():
    """
    Redirection function, that redirect to the wolfram page with latex request that user entered
    """
    if request.method == 'POST':
        data = request.json
        text = data["value"]
        if valid(text):
            # If text is valid than this text would be encoded to url
            redirected_page = MyStr('https://www.wolframalpha.com/input/?i=') + MyStr(
                urllib.parse.quote(text))
            res = {"url": str(redirected_page)}
            return jsonify(res)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
