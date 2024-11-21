from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Home path, next commit"

@app.route("/ingress")  # Add a new route to call ingress function
def ingress():
    return "ingress is working! sdodnls yup"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
