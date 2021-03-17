from forex_python.converter import CurrencyRates, CurrencyCodes


def validate(to,frm,amount):
    to_answer = check_valid_currency_type(to)
    from_answer = check_valid_currency_type(frm)
    amount_answer = check_valid_amount(amount)

    return{"To":to_answer, "From":from_answer, "Amount":amount_answer }

def check_valid_currency_type(currency):
    if currency.isnumeric():
        return [False,"Not a string"]
    if len(currency)==4:
        return [False,"not a valid Length"]
    
    
    currency=currency.upper()
    c = CurrencyRates()
    try:
        c.get_rates(currency)
        return [True, "Valid currency."]
    except:
        return [False, "invalid currency."]


def check_valid_amount(amount):
    if not(isinstance(amount, int) or isinstance(amount,float) or amount.isnumeric()):
        return[False, 'not a number']  
    if float(amount)<0:
        return [False, "Negative amount, must be positive"]
    else:
        return[True,'Valid Amount']

def convert(to, frm, amount):
    c= CurrencyRates()
    cc= CurrencyCodes()
    try: 
        converted_num = c.convert(frm.upper(), to.upper(), float(amount))
        symbol=cc.get_symbol(to.upper())
        return f"{symbol}{round(converted_num,2)}"
    except:
        return "something went wrong"

