from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name","World")
    return render_template("index.html", name = name)
@app.route("/Favorites", methods = ["POST"])
def Favorites():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    favoritegame = request.form.get("game")
    if not firstname or not lastname :
        return "Naspa!Baga ma dracu ce trebe acolo si apoi apasa submit"
    else:
       return render_template("succes.html")
    



if __name__ =="__main__":
    app.run()