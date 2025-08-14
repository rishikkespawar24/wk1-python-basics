from flask import Flask, render_template, request

app = Flask(__name__)

def calc(a: float, b: float, op: str) -> float:
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    return "Invalid operation"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            op = request.form["operation"]
            result = calc(a, b, op)
        except ValueError:
            result = "Please enter valid numbers"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
