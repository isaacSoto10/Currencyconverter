from unittest import TestCase
from python_helper import currency_help, display_help

class CurrencyHelper_TestCase(TestCase):
    def test_validate(self):
        self.assertEqual(currency_help.validate("USD","usd","50"),{'To': [True, 'Valid Currency.'], 'From': [True, 'Valid Currency.'], 'Amount': [True, 'Valid Amount.']})
        self.assertEqual(currency_help.validate("USD","hIi","50"),{'To': [True, 'Valid Currency.'], 'From': [False, 'Invalid Currency.'], 'Amount': [True, 'Valid Amount.']})
        self.assertEqual(currency_help.validate("USD","GBP","fifty"),{'To': [True, 'Valid Currency.'], 'From': [True, 'Valid Currency.'], 'Amount': [False, 'Not a number.']})
        self.assertEqual(currency_help.validate("Boog","GBP","50"),{'To': [False, 'Invalid Length.'], 'From': [True, 'Valid Currency.'], 'Amount': [True, 'Valid Amount.']})

    def test_check_valid_currency(self):
        self.assertTrue(currency_help.check_valid_currency_type("USD")[0])
        self.assertFalse(currency_help.check_valid_currency_type(20)[0])
        self.assertFalse(currency_help.check_valid_currency_type("20")[0])
        self.assertFalse(currency_help.check_valid_currency_type("USSR")[0])
        self.assertFalse(currency_help.check_valid_currency_type("WWW")[0])
    
    def test_check_valid_amount(self):
        self.assertTrue(currency_help.check_valid_amount(20)[0])
        self.assertTrue(currency_help.check_valid_amount("20")[0])
        self.assertFalse(currency_help.check_valid_amount(-20)[0])
        self.assertFalse(currency_help.check_valid_amount("Bob")[0])
    
    def test_convert(self):
        self.assertEqual(currency_help.convert("USD","USD",50),"US$50.0")


from app import app

class AppRoute_TestCase(TestCase):
    def test_home(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn("<h1>Currency Converter</h1>",html)

    def test_convert(self):
        with app.test_client() as client:
            res = client.post("/convert", data={"from-currency" : "USD", "to-currency" : "USD", "amount-currency" : "50"})
            print(res)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn("50",html)