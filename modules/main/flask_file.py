from flask import Flask, render_template, request


app = Flask(__name__, static_url_path="/lib", )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/friends_map", methods=["POST"])
def register():
    if request.method == 'POST':
        acc = request.form.get("account")
    return render_template("index.html")


app.run(debug=True, host='0.0.0.0', port=8080)
