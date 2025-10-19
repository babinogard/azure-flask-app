from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure App Service.\n This is X."

print("This is test: one, two, three!")

if __name__ == "__main__":
    app.run(debug=True)