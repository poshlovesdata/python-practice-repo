import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()




def fetch_exchange_rate(from_curr: str, to_curr: str, amount: float) -> float:
    try:
        base_url = 'https://api.exchangerate.host'
        currencies_source = 'currencies=NGN,EUR,GBP,PLN&source=USD'
        api_key = os.getenv('CONVERTER_API')
        conversion_endpoint = f'{base_url}/convert?access_key={api_key}&from={from_curr}&to={to_curr}&amount={amount}&format=1'
        
        result = requests.get(conversion_endpoint)
        data = result.json()
        output = f"""
        {amount} {from_curr} => {data['result']} {to_curr}
        """
    except requests.exceptions.ConnectionError as ce:
        print("Connection Errror: ")
    except requests.exceptions.HTTPError as he:
        print("HTTP Error occured")
    except requests.exceptions.InvalidURL as ie:
        print("Invalid URL: ")
    


if __name__ == "__main__":
    fetch_exchange_rate('USD', 'NGN', 10)
    

    