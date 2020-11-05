from flask import Flask, render_template

app = Flask(__name__)

#home screen
@app.route("/home")
@app.route("/")
def home():
  return render_template("home.html")

#playgrounds
@app.route("/playgrounds")
def playgrounds():
  return render_template("playgrounds.html")

#themes
@app.route("/themes")
def themes():
  return render_template("themes.html")

#github
@app.route("/github")
def github():
  return render_template("github.html")

#project plan
@app.route("/projectplan")
def projectplan():
  return render_template("projectplan.html")

@app.route("/image")
def images():
  return render_template("image.html")

@app.route("/rimages")
def rimages():
  return render_template("rimages.html")

@app.route("/trivia")
def trivia():
  return render_template("trivia.html")

@app.route("/rocks")
def rocks():
  return render_template("rocks.html")

@app.route("/randomnum")
def randomnum():
  return render_template("randomnum.html")

@app.route("/battleship")
def battleship():
  return render_template("battleship.html")

if __name__ == "__main__":
  app.run(debug=True, port='3000', host='0.0.0.0')