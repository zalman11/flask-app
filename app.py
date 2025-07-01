from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Simple Flask Web App!</h1><p>This is the home page.</p>"

@app.route("/hello")
def hello():
    user = request.args.get("user", "World")
    return f"<h2>Hello, {user}!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
