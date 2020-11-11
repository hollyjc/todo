from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "test string"
    
#if any errors they should pop up on the page
if __name__ == "__main__":
    app.run(debug=True)