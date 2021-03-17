from flask import Flask, request, render_template, redirect, flash, jsonify
#from flask_debugtoolbar import DebugToolbarExtension
from python_helper import currency_help, display_help

app = Flask(__name__)
app.config["SECRET_KEY"] = "mykey"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
#debug = DebugToolbarExtension(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/converter")
def convert_currency():
    data= request.args
    from_currency = data['from-currency']
    to_currency = data['to-currency']
    amount_currency= data['amount-currency']

    validation = currency_help.validate(to=to_currency,frm=from_currency,amount=amount_currency)
    for val in validation:
        if validation[val][0] == False:
            display_help.display_error(error=validation[val][1],preface="There was an error with your submission:",postface="Please try again.")
            return redirect("/")
    result= currency_help.convert(frm=from_currency, to=to_currency, amount=amount_currency)
    return render_template('home.html', convert=result)

