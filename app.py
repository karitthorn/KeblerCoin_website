from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") #index (Thai)
def indexthai():
    return render_template("indexth.html")

@app.route("/en") #index (English)
def indexenglish():
    return render_template("indexen.html")

@app.route("/whitepaper") #!don't use now
def whitepaper():
    return render_template("whitepaper.html")

@app.route("/buycoin")
def buycoin():
    return render_template("buycoin.html")

if __name__ == '__main__':
    app.run()
    

    
