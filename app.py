from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return "This is about page."

@app.route("/contact")
def contact():
    return "This is contact page"

print("This is test: one, two, three!")

if __name__ == "__main__":
    app.run(debug=True)