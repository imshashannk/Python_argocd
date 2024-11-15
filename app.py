from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "D"

@app.route("/ingress")  # Add a new route to call ingress function
def ingress():
    return "ingress is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
