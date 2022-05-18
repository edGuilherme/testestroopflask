from flask import Flask, render_template, url_for

app = Flask(__name__,  template_folder="templates")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")    

@app.route("/teladeaplicacao")
def teladeaplicacao():
    return render_template("teladeaplicacao.html")

@app.route("/descanso")
def descanso():
    return render_template("descanso.html")

@app.route("/final")
def final():
    return render_template("final.html")

@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html")

@app.route("/grafico")
def grafico():
    return render_template("grafico.html")   

if __name__ == '__main__':
    app.run(debug=True)

