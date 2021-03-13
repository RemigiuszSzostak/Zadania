from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def home():
    page = """
            <title>Kalkulator!</title>
            <h1>Wybierz operacje i podaj liczby.</h1>
            <form action="/score" method="POST">
                <input type="text" name="user_first_numb" />
                <select id="operator" name="operator">
                    <option value="sum"> + </option>
                    <option value="sub"> - </option>
                    <option value="multi"> * </option>
                    <option value="div"> / </option>
                <input type="text" name="user_second_numb" />  
                <button type="submit">Wyślij.</button>
            </form>

    """
    return page


@app.route('/score', methods=['POST'])
def welcome_page():


    value_a = request.form["user_first_numb"]
    value_b = request.form["user_second_numb"]
    value_a = int(value_a)
    value_b = int(value_b)
    value_c = request.form["operator"]
    
    if value_c == "+":
        x = value_a + value_b
    elif value_c == "-":
        x = value_a - value_b
    elif value_c == "*":
        x = value_a * value_b
    elif value_c == "/":
        if value_b == 0:
            x = "zero division error"
        else:
            x = value_a / value_b

    return f"Your score is: {x}"


app.run(debug=True)
