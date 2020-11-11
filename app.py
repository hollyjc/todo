from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#if any errors they should pop up on the page
if __name__ == "__main__":
    app.run(debug=True)