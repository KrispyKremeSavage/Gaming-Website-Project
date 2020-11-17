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

@app.route("/kailavideo")
def kailavideo():
  return render_template("kailavideo.html")

@app.route("/calvinvideo")
def calvinvideo():
  return render_template("calvinvideo.html")

@app.route("/kailasgoals")
def kailasgoals():
  return render_template("kailasgoals.html")

@app.route("/eshaangoals")
def eshaangoals():
  return render_template("eshaangoals.html")

@app.route("/brentgoals")
def brentgoals():
  return render_template("brentgoals.html")

@app.route("/calvingoals")
def calvingoals():
  return render_template("calvingoals.html")

@app.route("/gametest")
def gametest():
  return render_template("gametest.html")

@app.route("/eshaanvideo")
def eshaanvideo():
    return render_template("eshaanvideo.html")

@app.route("/pong")
def pong():
  return render_template("pong.html")

@app.route("/pacman")
def pacman():
  return render_template("pacman.html")

@app.route("/tics")
def tics():
  return render_template("tics.html")


if __name__ == "__main__":
  app.run(debug=True, port='3000', host='127.0.0.1')