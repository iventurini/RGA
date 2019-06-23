#fixerio
#I create this library to access fixerio endpoints (onlyt those available in free version)
#solo endpoints que estan disponibles en la version free 
import requests
from datetime import date

def _url(path):
    return 'http://data.fixer.io/api' + path

def get_latest(api_key,base='EUR',*symbols):
    symbols_list = ",".join(symbols)
    return requests.get(_url('/latest?access_key={}&base={}&symbols={}'.format(api_key,base,symbols_list)))
def get_historical(api_key, historicaldate= date.today(), base='EUR', *symbols):
    symbols_list = ",".join(symbols)
    return requests.get(_url('/{}?access_key={}&base={}&symbols={}'.format(historicaldate.strftime('%Y-%m-%d'),api_key,base,symbols_list)))
