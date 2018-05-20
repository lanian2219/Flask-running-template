from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def login():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
