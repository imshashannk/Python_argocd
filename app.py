from flask import Flask, request

app = Flask(__name__)

# Hardcoded secret key (vulnerability: sensitive data exposure)
SECRET_KEY = "hardcoded_secret_key_123"

@app.route("/")
def hello_world():
    # Reflect user input directly in the response (vulnerability: Cross-Site Scripting - XSS)
    name = request.args.get("name", "Worldslkfjwashfliuszohawbhfoidslkvbgfwhakvlnjks")
    return f"Hello, {name}! Welcome to the home path."

@app.route("/login", methods=["POST"])
def login():
    # Hardcoded credentials (vulnerability: insecure authentication)
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == "password123":
        return "Login successful!"
    return "Invalid credentials!", 401

@app.route("/query", methods=["GET"])
def query_db():
    # Vulnerable to SQL Injection (vulnerability: directly using user input in SQL query)
    user_input = request.args.get("user", "default_user")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # Dangerous use of input
    # Simulating a database response
    return f"Query executed: {query}"

@app.route("/ingress")
def ingress():
    # Open redirect vulnerability
    next_url = request.args.get("next", "/")
    return f'<a href="{next_url}">Click here to proceed</a>'

@app.route("/exec")
def execute():
    # Command Injection Vulnerability
    command = request.args.get("cmd", "echo 'Hello'")
    result = os.popen(command).read()  # Direct execution of user-provided input
    return f"Command executed: {result}"

if __name__ == "__main__":
    # Debug mode enabled (vulnerability: sensitive debug info exposure)
    app.run(host="0.0.0.0", port=80, debug=True)
