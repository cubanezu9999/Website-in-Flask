from flask import Flask,redirect, render_template, request

app = Flask(__name__)

peoples = []


@app.route("/")
def home():
    name = request.args.get("name","World")
    return render_template("index.html", name = name)

@app.route("/Inreg")
def reg():
    return render_template("inreg.html", peoples=peoples)

@app.route("/Favorites", methods = ["POST"])
def Favorites():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    game = request.form.get("game")
    if not firstname or not lastname :
        return render_template("failure.html")
    
       
    peoples.append(f"{firstname} {lastname} ii place sa joace {game}")
    return redirect("/Inreg")
    



if __name__ =="__main__":
    app.run()