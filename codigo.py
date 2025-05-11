from flask import Flask, render_template, request

app = Flask(__name__)
agendamentos = []

@app.route("/")
def index():
    return render_template("agendamento.html", agendamentos=agendamentos)

@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form["nome"]
    data = request.form["data"]
    agendamentos.append({"nome": nome, "data": data})
    return render_template("agendamento.html", agendamentos=agendamentos)

if __name__ == "__main__":
    app.run(debug=True)
